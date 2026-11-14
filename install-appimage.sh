#!/bin/bash
# Installe l'AppImage de GOD dans le menu des applications.
# Usage : ./install-appimage.sh chemin/vers/GOD-x86_64.AppImage
set -e

[ -n "$1" ] && [ -f "$1" ] || { echo "Usage : $0 chemin/vers/GOD-x86_64.AppImage"; exit 1; }

INSTALL_DIR="$HOME/.local/share/GOD"
APPS_DIR="$HOME/.local/share/applications"
mkdir -p "$INSTALL_DIR" "$APPS_DIR"

cp "$1" "$INSTALL_DIR/GOD.AppImage"
chmod +x "$INSTALL_DIR/GOD.AppImage"

# Icône : extraite de l'AppImage elle-même
TMP="$(mktemp -d)"
if (cd "$TMP" && "$INSTALL_DIR/GOD.AppImage" --appimage-extract GOD.png >/dev/null 2>&1) \
   && [ -f "$TMP/squashfs-root/GOD.png" ]; then
    cp "$TMP/squashfs-root/GOD.png" "$INSTALL_DIR/GOD.png"
else
    echo "Icône non extraite : le lanceur n'aura pas d'icône."
fi
rm -rf "$TMP"

cat > "$APPS_DIR/GOD.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=GOD
Comment=God Offers Downloads
Exec="$INSTALL_DIR/GOD.AppImage"
Icon=$INSTALL_DIR/GOD
Categories=AudioVideo;
Terminal=false
StartupWMClass=God
EOF

update-desktop-database "$APPS_DIR" 2>/dev/null || true
echo "Installé dans $INSTALL_DIR, lanceur : $APPS_DIR/GOD.desktop"
