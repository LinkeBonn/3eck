# 🚩 Dreieckständer-Tracker für DIE LINKE Bonn

Ein einfaches Flask-Webtool zum Erfassen, Verwalten und Anzeigen von Dreieckständern im Stadtgebiet Bonn.  
Optimiert für mobile Nutzung, inkl. Karte, Übersicht, Status-Farben, Löschfunktion und CSV-Export.

---

## 🔧 Features

- 📍 Einträge mit GPS-Koordinaten und Adress-Suche
- 📸 Foto-Upload direkt vom Handy (Kamera/Galerie)
- 🗺️ Kartenansicht aller gemeldeten Ständer
- ✅ Status: „Gut“, „Kaputt“, „Offen“
- 🏘 OG-Zuordnung 
- 🔐 Passwortgeschütztes Löschen
- 📊 Statistikseite mit Eintragszählern
- ℹ️ Anleitung & FAQ mit Screenshots

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
```

Die App läuft unter [http://localhost:5000](http://localhost:5000)

---

## 🐳 Docker / Compose

### Starten mit Docker Compose:

```bash
docker compose up --build
```

Oder standalone:

```bash
docker build -t dreieckstaender .
docker run -p 5000:5000 dreieckstaender
```

---

## 📁 Datenstruktur

- Einträge werden als `daten.csv` im Root gespeichert
- Bilder liegen unter `static/images/`
- Screenshots für die Anleitung: `static/screenshots/`

---

## 🔐 Löschfunktion

Beim Eintragen wird ein zufälliges Passwort angezeigt.  
Dieses kann später zum Löschen des Eintrags verwendet werden.  
**Wird das Passwort vergessen, ist eine manuelle Entfernung nötig.**



