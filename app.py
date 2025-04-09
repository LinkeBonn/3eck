from flask import Flask, render_template, request, redirect, url_for, flash
import csv, os
from datetime import datetime
from werkzeug.utils import secure_filename
import secrets

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
DATA_FILE = 'daten.csv'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.secret_key = 'etwas-geheimes'

# 🔸 Startseite (nur Formular)
@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

# 🔸 Eintrag verarbeiten & CSV schreiben
@app.route('/submit', methods=['POST'])
def submit():
    passwort = secrets.token_hex(3)
    titel = request.form.get('titel')
    status = request.form.get('status')
    kommentar = request.form.get('kommentar')
    lat = request.form.get('latitude')
    lon = request.form.get('longitude')
    strasse = request.form.get('strasse')
    plz = request.form.get('plz')
    stadt = request.form.get('stadt')
    og = request.form.get('og')
    bild = request.files['bild']

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    bildname = f"{timestamp}_{secure_filename(bild.filename)}"
    bildpfad = os.path.join(UPLOAD_FOLDER, bildname)
    bild.save(bildpfad)

    write_header = not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0
    with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['Titel', 'Status', 'Kommentar', 'Latitude', 'Longitude', 'Straße', 'PLZ', 'Stadt','OG', 'Bild', 'Zeitstempel', 'Passwort'])
        writer.writerow([titel, status, kommentar, lat, lon, strasse, plz, stadt, og, bildname, timestamp, passwort])

    flash(f'Dein Löschcode für {titel}: {passwort}', 'info')
    return redirect(url_for('view'))

# 🔸 Übersicht anzeigen
@app.route('/view')
def view():
    eintraege = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                eintraege.append({
                    'titel': row[0],
                    'status': row[1],
                    'kommentar': row[2],
                    'lat': row[3],
                    'lon': row[4],
                    'strasse': row[5],
                    'plz': row[6],
                    'stadt': row[7],
                    'og': row[8],
                    'bild': row[9],
                    'timestamp': row[10],
                    'passwort': row[11]
                })
    return render_template('view.html', eintraege=eintraege)

# 🔸 Eintrag löschen
@app.route('/delete/<string:timestamp>', methods=['POST'])
def delete_entry(timestamp):
    pw = request.form.get('passwort')
    new_rows = []
    deleted = False

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row[10] == timestamp and row[11] == pw:
                deleted = True
                try:
                    os.remove(os.path.join(UPLOAD_FOLDER, row[9]))
                except:
                    pass
                continue
            new_rows.append(row)

    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_rows)

    flash("Eintrag erfolgreich gelöscht." if deleted else "Löschen fehlgeschlagen. Passwort falsch?", "success" if deleted else "danger")
    return redirect(url_for('view'))

# 🔸 Kartenansicht
@app.route('/map')
def map_view():
    eintraege = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                eintraege.append({
                    'titel': row[0],
                    'lat': float(row[3]),
                    'lon': float(row[4]),
                    'status': row[1],
                    'og': row[8]
                })
    return render_template('map.html', eintraege=eintraege)


@app.route('/stats')
def stats():
    ogs = ['OG Beuel', 'OG Süd', 'OG Nord', 'OG WestEndPop']
    status_keys = ['Gut', 'Kaputt', 'Offen']

    stats_data = {
        'gesamt': 0,
        'ogs': {og: 0 for og in ogs},
        'status': {s: 0 for s in status_keys}
    }

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                stats_data['gesamt'] += 1
                og = row[8]
                status = row[1].split()[0]
                if og in stats_data['ogs']:
                    stats_data['ogs'][og] += 1
                if status in stats_data['status']:
                    stats_data['status'][status] += 1

    return render_template('stats.html', stats=stats_data)

@app.route('/faq')
def faq():
    return render_template('faq.html')

# 🔸 Starten
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
