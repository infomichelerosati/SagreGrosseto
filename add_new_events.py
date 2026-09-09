import csv

lines = []
new_events = [
    [
        "20/07/2026",
        "26/07/2026",
        "Sagra della Lumaca e della Cucina Maremmana",
        "Capalbio (Fraz. Chiarone Scalo)",
        "Circolo Il Mare, Chiarone Scalo",
        "43ª edizione dedicata alle ricette tradizionali maremmane. Lumaca proposta al sugo o fritta, oltre a tortelli, carne alla brace e acquacotta.",
        "Tutti i giorni",
        "⭐⭐⭐⭐ (4.3)"
    ],
    [
        "21/07/2026",
        "26/07/2026",
        "Sagra del Picio, della Donzella e della Rostinciana",
        "Follonica",
        "Pineta di Ponente (Palazzi Rossi), Follonica",
        "Organizzata dal Follonica Hockey nell'ambito della Festa dello Sport. Specialità: pici freschi, donzella e saporita rostinciana alla brace.",
        "Tutti i giorni",
        "⭐⭐⭐⭐ (4.2)"
    ],
    [
        "08/08/2026",
        "14/08/2026",
        "Sagra della Salsiccia",
        "Orbetello",
        "Stadio Ottorino Vezzosi (ex-idroscalo), Orbetello",
        "Serate dedicate alla cucina maremmana con protagonista la salsiccia (alla griglia, in umido con fagioli o polenta) e musica dal vivo.",
        "Tutti i giorni",
        "⭐⭐⭐⭐ (4.1)"
    ],
    [
        "23/07/2026",
        "12/08/2026",
        "Sagra del Baccalà",
        "Magliano in Toscana (Fraz. Sant'Andrea)",
        "Campo Sportivo, Sant'Andrea al Civilesco",
        "Storica rassegna (35ª edizione) incentrata sul baccalà in tutte le salse e piatti tipici maremmani. Chiusa il 2 agosto.",
        "Tutti i giorni (tranne il 2 agosto)",
        "⭐⭐⭐⭐½ (4.6)"
    ]
]

with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        lines.append(row)

with open('sagre.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in lines:
        writer.writerow(row)
    for new_row in new_events:
        writer.writerow(new_row)

print("Script completato.")
