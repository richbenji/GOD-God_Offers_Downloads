# Recréer l'appimage de GOD
# Commande : ./rebuild_appimage.sh
source venv/bin/activate
pyinstaller --clean GOD.spec
cp dist/GOD AppDir/usr/bin/GOD
chmod +x AppDir/usr/bin/GOD
chmod +x AppDir/AppRun
chmod +x AppDir/usr/bin/GOD
appimagetool AppDir
deactivate

