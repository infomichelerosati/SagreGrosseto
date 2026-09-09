import csv

new_events = [
    [
        "10/08/2026",
        "13/08/2026",
        "Sagra della Frittura di Pesce",
        "Orbetello (Fraz. Fonteblanda)",
        "Campo Sportivo, Via dello Stadio, Fonteblanda",
        "Prima parte del celebre evento gastronomico estivo dell'ASD Fonteblanda. Protagonista assoluta la frittura espressa di paranza e calamari, dorata e croccante. Stand aperti dalle 19:30, seguiti da musica dal vivo e ballo liscio.",
        "Tutti i giorni",
        "⭐⭐⭐⭐½ (4.5)"
    ],
    [
        "16/08/2026",
        "25/08/2026",
        "Sagra del Cacciucco",
        "Orbetello (Fraz. Fonteblanda)",
        "Campo Sportivo, Via dello Stadio, Fonteblanda",
        "Seconda tranche dell'evento clou di Fonteblanda. Il menù si arricchisce con il tradizionale Cacciucco alla maremmana, primi ai frutti di mare e alternative di carne. Apertura stand ore 19:30, area ballo e orchestre tutte le sere.",
        "Tutti i giorni",
        "⭐⭐⭐⭐½ (4.5)"
    ]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for new_row in new_events:
        writer.writerow(new_row)

print("Eventi di Fonteblanda aggiunti con successo.")
