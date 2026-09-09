import csv

events = [
    ["09/07/2026", "09/07/2026", "Calici sotto il Castello", "Roccastrada (Fraz. Montemassi)", "Vie e piazze del centro storico, Montemassi", "Dalle 20:00, evento dedicato al vino e al territorio con 15 produttori locali, punti gastronomici e musica dal vivo.", "Singola serata", "⭐⭐⭐⭐ (4.4)"],
    ["09/07/2026", "09/07/2026", "Spettacolo \"La Traviata\"", "Massa Marittima", "Cortile della biblioteca, Massa Marittima", "Spettacolo musicale e teatrale incentrato su La Traviata. Inizio ore 21:15.", "Singola serata", "⭐⭐⭐⭐ (4.3)"],
    ["09/07/2026", "09/07/2026", "Escursione Archeologica a La Cote Ciombella", "Isola del Giglio", "Sito archeologico preistorico La Cote Ciombella, Isola del Giglio", "Escursione guidata archeo-naturalistica e sensoriale al tramonto. Prenotazione obbligatoria.", "Singola serata", "⭐⭐⭐⭐½ (4.6)"]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for ev in events:
        writer.writerow(ev)
