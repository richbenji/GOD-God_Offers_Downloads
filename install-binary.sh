#!/bin/bash
# Installe GOD dans ~/.local/share/GOD et crée un lanceur dans le menu.
# Usage : ./install.sh [chemin/vers/GOD]   (par défaut : le fichier GOD à côté du script)
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="${1:-$SCRIPT_DIR/GOD}"
[ -f "$SRC" ] || { echo "Usage : $0 [chemin/vers/GOD]"; exit 1; }
SRC="$(realpath "$SRC")"

INSTALL_DIR="$HOME/.local/share/GOD"
APPS_DIR="$HOME/.local/share/applications"
mkdir -p "$INSTALL_DIR" "$APPS_DIR"

# Binaire
cp "$SRC" "$INSTALL_DIR/GOD"
chmod +x "$INSTALL_DIR/GOD"

# Icône : à côté du script, ou dans le dépôt
ICON=""
for candidate in \
    "$SCRIPT_DIR/GOD.png" \
    "$SCRIPT_DIR/AppDir/GOD.png" \
    "$SCRIPT_DIR/GOD/assets/logos/GOD.png"; do
    if [ -f "$candidate" ]; then ICON="$candidate"; break; fi
done
if [ -n "$ICON" ]; then
    cp "$ICON" "$INSTALL_DIR/GOD.png"
else
    echo "GOD.png introuvable : le lanceur n'aura pas d'icône."
fi

cat > "$APPS_DIR/GOD.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=GOD
Comment=God Offers Downloads
Exec="$INSTALL_DIR/GOD"
Icon=$INSTALL_DIR/GOD.png
Categories=AudioVideo;
Terminal=false
StartupWMClass=God
EOF

update-desktop-database "$APPS_DIR" 2>/dev/null || true
echo "Installé dans $INSTALL_DIR, lanceur : $APPS_DIR/GOD.desktop"
