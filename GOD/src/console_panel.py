"""Console intégrée : reprend ce que le programme écrit dans le terminal."""
import queue
import re
import sys
import tkinter as tk
import tkinter.font as tkfont

import customtkinter as ctk

_ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]")
_output_queue = queue.Queue()   # (flux, texte) ; thread-safe, lue par l'UI


class _Tee:
    """Remplace sys.stdout / sys.stderr : écrit dans le vrai terminal ET dans la file."""

    def __init__(self, original, tag):
        self._original = original
        self._tag = tag

    def write(self, text):
        if not text:
            return 0
        if self._original is not None:
            try:
                self._original.write(text)
            except Exception:
                pass
        _output_queue.put((self._tag, text))
        return len(text)

    def flush(self):
        if self._original is not None:
            try:
                self._original.flush()
            except Exception:
                pass

    def isatty(self):
        return False    # évite les codes couleur ANSI dans la console

    def __getattr__(self, name):
        original = self.__dict__.get("_original")
        # "buffer" est volontairement caché : yt-dlp écrirait alors directement dans le
        # vrai terminal en contournant write(), et la console ne verrait rien.
        if original is None or name == "buffer":
            raise AttributeError(name)
        return getattr(original, name)


def install_capture():
    if not isinstance(sys.stdout, _Tee):
        sys.stdout = _Tee(sys.stdout, "out")
    if not isinstance(sys.stderr, _Tee):
        sys.stderr = _Tee(sys.stderr, "err")


# Installé dès l'import : ce qui est affiché avant la création de la fenêtre
# est mis en file d'attente et apparaîtra dans la console.
install_capture()


class ConsolePanel(ctk.CTkFrame):
    MIN_HEIGHT = 80
    DEFAULT_HEIGHT = 60
    POLL_MS = 100
    MAX_ITEMS_PER_TICK = 2000

    def __init__(self, parent):
        super().__init__(parent)
        self._expanded = False
        self._height = self.DEFAULT_HEIGHT
        self._drag_start = None
        self._cr_pending = False   # '\r' reçu : la prochaine écriture remplace la ligne

        # Poignée de redimensionnement (visible seulement quand la console est dépliée)
        self._grip = tk.Frame(self, height=6, bg="#6b6b6b", cursor="sb_v_double_arrow")
        self._grip.bind("<ButtonPress-1>", self._start_drag)
        self._grip.bind("<B1-Motion>", self._on_drag)

        # En-tête
        self._header = ctk.CTkFrame(self, fg_color="transparent")
        self._header.pack(fill="x", padx=6, pady=4)

        self._toggle_btn = ctk.CTkButton(
            self._header, text="▶ Console", width=110, height=24, command=self.toggle
        )
        self._toggle_btn.pack(side="left")

        self._clear_btn = ctk.CTkButton(
            self._header, text="🗑️", width=40, height=24, command=self.clear
        )

        # Zone de texte (monospace, sans retour à la ligne, lecture seule)
        family = tkfont.nametofont("TkFixedFont").actual("family")
        self.textbox = ctk.CTkTextbox(
            self, height=self._height, wrap="none", font=(family, 11)
        )
        self.textbox.tag_config("err", foreground="#ff7b72")
        self.textbox.configure(state="disabled")

        self.after(self.POLL_MS, self._poll)

    # ---------------- affichage / repli ----------------
    def toggle(self):
        self.set_expanded(not self._expanded)

    def set_expanded(self, expanded):
        self._expanded = expanded
        if expanded:
            self._toggle_btn.configure(text="▼ Console")
            self._clear_btn.pack(side="left", padx=(6, 0))
            self._grip.pack(fill="x", padx=60, pady=(3, 0), before=self._header)
            self.textbox.pack(fill="x", padx=6, pady=(0, 6))
            self.textbox.see("end")
        else:
            self._toggle_btn.configure(text="▶ Console")
            self._clear_btn.pack_forget()
            self._grip.pack_forget()
            self.textbox.pack_forget()

    # ---------------- redimensionnement ----------------
    def _start_drag(self, event):
        self._drag_start = (event.y_root, self._height)

    def _on_drag(self, event):
        if not self._drag_start:
            return
        start_y, start_h = self._drag_start
        max_h = max(self.MIN_HEIGHT, self.winfo_toplevel().winfo_height() - 450)
        new_h = int(max(self.MIN_HEIGHT, min(max_h, start_h + (start_y - event.y_root))))
        self._height = new_h
        self.textbox.configure(height=new_h)

    # ---------------- contenu ----------------
    def clear(self):
        self._drain()   # ce qui est déjà en file passe avant l'effacement
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.configure(state="disabled")
        self._cr_pending = False

    def _poll(self):
        try:
            self._drain()
        except Exception:
            pass   # jamais d'erreur ici : elle repartirait dans la console
        self.after(self.POLL_MS, self._poll)

    def _drain(self):
        items = []
        try:
            for _ in range(self.MAX_ITEMS_PER_TICK):
                items.append(_output_queue.get_nowait())
        except queue.Empty:
            pass
        if not items:
            return

        # Fusionne les morceaux consécutifs du même flux (une seule insertion)
        merged = []
        for tag, text in items:
            if merged and merged[-1][0] == tag:
                merged[-1][1] += text
            else:
                merged.append([tag, text])

        at_bottom = self.textbox.yview()[1] >= 0.999   # ne pas "voler" le scroll si on relit
        self.textbox.configure(state="normal")
        for tag, text in merged:
            self._write(text, tag)
        self.textbox.configure(state="disabled")
        if at_bottom:
            self.textbox.see("end")

    def _write(self, text, tag):
        text = _ANSI_RE.sub("", text)
        text = text.replace("\r\n", "\n")
        if self._cr_pending and text.startswith("\n"):
            self._cr_pending = False   # '\r' et '\n' coupés entre deux lots

        # '\r' seul = retour en début de ligne (ligne de progression de yt-dlp) :
        # la ligne en cours est remplacée plutôt que dupliquée.
        for i, part in enumerate(text.split("\r")):
            if i > 0:
                self._cr_pending = True
            if not part:
                continue
            if self._cr_pending:
                self.textbox.delete("end-1c linestart", "end-1c")
                self._cr_pending = False
            self.textbox.insert("end", part, tag)