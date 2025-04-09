# 🚩 Dreieckständer-Tracker für DIE LINKE Bonn

Ein einfaches Flask-Webtool zum Erfassen, Verwalten und Anzeigen von Dreieckständern im Stadtgebiet Bonn.  
Optimiert für mobile Nutzung, inkl. Karte, Übersicht, Status-Farben, Löschfunktion und CSV-Export.

---

## 🔧 Features

- 📍 Einträge mit GPS-Koordinaten und Adress-Suche
- 📸 Foto-Upload direkt vom Handy (Kamera/Galerie)
- 🗺️ Kartenansicht aller gemeldeten Ständer
- ✅ Status: „Gut“, „Kaputt“, „Offen“
- 🏘 OG-Zuordnung (Beuel, Süd, Nord, WestEndPop)
- 🔐 Passwortgeschütztes Löschen
- 📊 Statistikseite mit Eintragszählern
- ℹ️ Anleitung & FAQ mit Screenshots
- 🔒 Läuft hinter Traefik mit HTTPS

---

## 🚀 Starten (lokal)

### Voraussetzung:

- Python 3.9+
- pip (oder venv)

### Setup:

```bash
git clone https://github.com/dein-user/dreieckstaender-tracker.git
cd dreieckstaender-tracker
pip install -r requirements.txt
python app.py
