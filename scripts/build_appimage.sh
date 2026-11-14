#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

source venv/bin/activate

APP_NAME="GOD"
ARCH="x86_64"
ICON_NAME="GOD.png"
PROJECT_ROOT="$(pwd)"

echo "🧹 Nettoyage..."
rm -rf build dist AppDir *.AppImage

echo "⬇️ Runtime (deno)..."
[ -x GOD/resources/runtime/linux/deno ] || python3 scripts/fetch_runtime.py

echo "🐍 Build PyInstaller..."
pyinstaller --clean GOD.spec

echo "📦 Création AppDir..."
mkdir -p AppDir/usr/bin
mkdir -p AppDir/usr/share/icons/hicolor/256x256/apps

echo "➡️ Copie du binaire..."
cp dist/GOD AppDir/usr/bin/GOD
chmod +x AppDir/usr/bin/GOD

echo "🎨 Icône..."
cp GOD/assets/logos/${ICON_NAME} AppDir/
cp GOD/assets/logos/${ICON_NAME} AppDir/usr/share/icons/hicolor/256x256/apps/

echo "📝 Desktop file..."
cat > AppDir/GOD.desktop <<EOF
[Desktop Entry]
Type=Application
Name=GOD
Comment=God Offers Downloads
Exec=GOD
Icon=GOD
Categories=AudioVideo;
Terminal=false
EOF

echo "🚀 AppRun..."
cat > AppDir/AppRun <<'EOF'
#!/bin/sh
HERE="$(dirname "$(readlink -f "$0")")"
exec "$HERE/usr/bin/GOD"
EOF

chmod +x AppDir/AppRun

echo "📦 Génération AppImage..."
appimagetool AppDir

echo "✅ AppImage créé : ${APP_NAME}-${ARCH}.AppImage"
