import csv

events = [
    [
        "17/07/2026",
        "19/07/2026",
        "Festa della Birra e Sagra dello Gnocco",
        "Roccalbegna",
        "Area Feste, Roccalbegna",
        "Festa estiva dedicata agli gnocchi fatti a mano e ottima birra, accompagnata da musica dal vivo e divertimento.",
        "Solo fine settimana",
        "⭐⭐⭐⭐ (4.3)"
    ],
    [
        "17/07/2026",
        "26/07/2026",
        "Tortelli & Calamari in Ecofesta",
        "Castiglione della Pescaia",
        "Palasport Casa Mora, Castiglione della Pescaia",
        "Un perfetto connubio tra i sapori di terra (tortelli maremmani) e mare (calamari) in un evento attento all'ambiente.",
        "Solo fine settimana",
        "⭐⭐⭐⭐½ (4.5)"
    ],
    [
        "08/08/2026",
        "08/08/2026",
        "Concerto al Teatro delle Rocce (Francesca Michielin)",
        "Gavorrano",
        "Teatro delle Rocce, Gavorrano",
        "La suggestiva cornice del teatro all'aperto ricavato in un'antica cava ospita grandi concerti della stagione estiva.",
        "Singola serata",
        "⭐⭐⭐⭐⭐ (4.8)"
    ]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for event in events:
        writer.writerow(event)
