import csv

lines = []
new_events = [
    [
        "17/07/2026",
        "18/07/2026",
        "Un mare di Birra",
        "Orbetello (Fraz. Talamone)",
        "Porto e Piazza, Talamone",
        "Festa estiva dedicata alle birre artigianali, accompagnata da street food, musica e intrattenimento nel suggestivo scenario di Talamone.",
        "Solo fine settimana",
        "⭐⭐⭐⭐ (4.1)"
    ]
]

with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 3:
            lines.append(row)
            continue
            
        nome = row[2]
        
        # Rimuovi Moscardino
        if "Sagra del Moscardino e del Polpetto" in nome:
            continue
            
        # Modifica Campagnatico
        if "Sagra di Campagnatico" in nome:
            row[0] = "24/07/2026"
            row[1] = "02/08/2026"
            row[2] = "Sagra dei Tortelli, Pici, Strozzapreti e Lumache"
            
        # Modifica Monterotondo
        if "Sagra del Maiale e della Pecora" in nome:
            row[0] = "17/07/2026"
            row[1] = "26/07/2026"
            row[6] = "Solo fine settimana"
            
        lines.append(row)

with open('sagre.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in lines:
        writer.writerow(row)
    for new_row in new_events:
        writer.writerow(new_row)

print("Script completato.")
