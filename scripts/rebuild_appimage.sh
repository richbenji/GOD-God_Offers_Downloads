#!/bin/bash

# Recréer l'appimage de GOD
# Commande : ./rebuild_appimage.sh

# Dit au script de s’arrêter dès qu’une commande échoue. Sans lui, un script shell continue même après une erreur. Par exemple, si pyinstaller plante, le script copie quand même l’ancien dist/GOD (ou échoue sur la copie), puis appimagetool reconstruit l’AppImage avec un binaire périmé, sans que tu t’en rendes compte. Avec set -e, tu vois l’erreur au bon endroit et rien d’autre ne s’exécute derrière.
set -e
cd "$(dirname "$0")/.."  # lancer le script depuis n’importe quel dossier. Sans le "cd", le script ne marchera pas si je le lance d'un autre dossier car j'utilise des chemins relatifs.
source venv/bin/activate
[ -x GOD/resources/runtime/linux/deno ] || python scripts/fetch_runtime.py
pyinstaller --clean GOD.spec
cp dist/GOD AppDir/usr/bin/GOD
chmod +x AppDir/usr/bin/GOD
chmod +x AppDir/AppRun
appimagetool AppDir
deactivate  # deactivate est inutile. Le script tourne dans son propre processus, donc le venv s’efface tout seul à la fin. Tu peux le laisser, ça ne gêne pas.

