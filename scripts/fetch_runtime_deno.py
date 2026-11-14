"""Télécharge deno dans resources/runtime/<os>/ (à lancer avant le build)."""
import hashlib
import platform
import stat
import sys
import urllib.request
import zipfile
from io import BytesIO
from pathlib import Path

VERSION = "latest"  # ou "v2.x.y" pour figer une version
DEST_ROOT = Path(__file__).resolve().parent.parent / "GOD" / "resources" / "runtime"

TARGETS = {
    ("Linux", "x86_64"): ("deno-x86_64-unknown-linux-gnu.zip", "linux", "deno"),
    ("Windows", "AMD64"): ("deno-x86_64-pc-windows-msvc.zip", "windows", "deno.exe"),
    ("Darwin", "arm64"): ("deno-aarch64-apple-darwin.zip", "macos", "deno"),
    ("Darwin", "x86_64"): ("deno-x86_64-apple-darwin.zip", "macos", "deno"),
}


def main():
    key = (platform.system(), platform.machine())
    if key not in TARGETS:
        sys.exit(f"Plateforme non prévue : {key}")
    asset, os_dir, exe = TARGETS[key]

    base = "https://github.com/denoland/deno/releases/" + (
        "latest/download" if VERSION == "latest" else f"download/{VERSION}"
    )
    data = urllib.request.urlopen(f"{base}/{asset}").read()
    expected = urllib.request.urlopen(f"{base}/{asset}.sha256sum").read().decode().split()[0]
    if hashlib.sha256(data).hexdigest() != expected:
        sys.exit("Somme sha256 incorrecte : téléchargement abandonné.")

    dest = DEST_ROOT / os_dir
    dest.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(BytesIO(data)) as zf:
        (dest / exe).write_bytes(zf.read(exe))
    (dest / exe).chmod((dest / exe).stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print(f"OK : {dest / exe}")


if __name__ == "__main__":
    main()
