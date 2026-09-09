import csv

# Le 3 righe da aggiornare e i nuovi valori
updates = {
    "Festa nell'Aia": {"start": "16/07/2026", "end": "19/07/2026"},
    "Medioevo nel Borgo": {"start": "07/08/2026", "end": "09/08/2026"},
    "Palio dei Ciuchi": {"start": "13/08/2026", "end": "14/08/2026"}
}

# I nuovi eventi da appendere
new_events = [
    ["03/07/2026","04/07/2026","Festa della Birra","Roccastrada (Fraz. Roccatederighi)","San Martino, Roccatederighi","Serate dedicate alla birra artigianale, pizze, gastronomia locale e dj set sotto i freschi castagni di San Martino. Stand aperti dalle 19:00.","Solo fine settimana","⭐⭐⭐⭐ (4.4)"],
    ["10/07/2026","12/07/2026","Sagra del Piatto Povero","Roccastrada (Fraz. Torniella)","Centro Storico, Torniella","Celebrazione della cultura contadina con piatti poveri e genuini come l'acquacotta, la pappa al pomodoro e gli spaghetti con le briciole. Stand dalle 19:30.","Solo fine settimana","⭐⭐⭐⭐ (4.3)"],
    ["10/07/2026","12/07/2026","Festa dei Cacciatori","Roccastrada (Fraz. Roccatederighi)","Area Feste, Roccatederighi","Stand gastronomici aperti dalle 19:30, dedicati alla cacciagione e al cinghiale, per celebrare le tradizioni venatorie dell'alta Maremma.","Solo fine settimana","⭐⭐⭐⭐½ (4.5)"],
    ["08/08/2026","09/08/2026","Torneo di Palla Eh!","Roccastrada (Fraz. Torniella)","Piazze e vicoli del borgo, Torniella","Storico e affascinante gioco sferistico a mani nude per le vie del borgo, un antico antenato del tennis tramandato nei secoli. Partite nel pomeriggio/sera.","Solo weekend","⭐⭐⭐⭐½ (4.7)"],
    ["08/08/2026","16/08/2026","Sagra del Maccherone","Roccastrada (Fraz. Sassofortino)","Parco Fonte di Vandro, Sassofortino","Protagonista assoluto il maccherone fatto a mano al fresco del parco. Aperta 8-9 e 14-16 agosto dalle 19:30 (il 15 anche a pranzo).","Solo weekend e Ferragosto","⭐⭐⭐⭐½ (4.6)"],
    ["16/08/2026","16/08/2026","Concerto della Banda","Roccastrada (Fraz. Torniella)","Piazza del Popolo, Torniella","Tradizionale concerto bandistico serale post-Ferragosto per allietare il borgo. Inizio previsto ore 21:30.","Singola serata","⭐⭐⭐⭐ (4.2)"],
    ["20/08/2026","20/08/2026","Spettacolo Teatrale","Roccastrada (Fraz. Torniella)","Centro Storico, Torniella","Spettacolo teatrale serale all'aperto (inizio ore 21:15 circa) all'interno delle iniziative estive della Pro Loco Piloni-Torniella.","Singola serata","⭐⭐⭐⭐ (4.3)"],
    ["22/08/2026","23/08/2026","Torneo di Palla Eh!","Roccastrada (Fraz. Piloni)","Piazza del borgo, Piloni","Tappa a Piloni dell'antico torneo itinerante di palla a 21 giocato per le piazze del paese. Le sfide animeranno il borgo nel fine settimana.","Solo weekend","⭐⭐⭐⭐½ (4.6)"]
]

lines = []
with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 2:
            name = row[2]
            for key, val in updates.items():
                if key in name:
                    row[0] = val["start"]
                    row[1] = val["end"]
        lines.append(row)

with open('sagre.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in lines:
        writer.writerow(row)
    for new_row in new_events:
        writer.writerow(new_row)

print("CSV aggiornato con successo.")
