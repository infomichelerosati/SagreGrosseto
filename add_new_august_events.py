import csv

new_events = [
    [
        "09/08/2026",
        "16/08/2026",
        "Sagra dei Pici e dello Zafferano",
        "Manciano (Fraz. Marsiliana)",
        "Marsiliana",
        "Sagra dedicata a un abbinamento particolarissimo: i pici fatti a mano accompagnati dallo zafferano purissimo coltivato localmente nella Maremma.",
        "Tutte le sere",
        "⭐⭐⭐⭐½ (4.4)"
    ],
    [
        "07/08/2026",
        "09/08/2026",
        "Stortellata Sammartinese & Festa della Birra",
        "Manciano (Fraz. San Martino sul Fiora)",
        "San Martino sul Fiora",
        "Doppio appuntamento che unisce i classici tortelli maremmani (la 'stortellata') con una vivace festa della birra e musica dal vivo.",
        "Sera",
        "⭐⭐⭐⭐ (4.1)"
    ],
    [
        "13/08/2026",
        "15/08/2026",
        "Notti di Pinte",
        "Scansano",
        "Piazzale Le Cascine, Scansano",
        "Serate di mezza estate dedicate alla birra artigianale, accompagnate da ottima musica dal vivo e gustosi stand gastronomici nel cuore del paese del Morellino.",
        "Dalle 19:00",
        "⭐⭐⭐⭐ (4.2)"
    ],
    [
        "08/08/2026",
        "23/08/2026",
        "Sagra della Panzanella",
        "Semproniano",
        "Centro storico, Semproniano",
        "Ben 15 giorni di festa dedicati al piatto fresco e povero della tradizione contadina toscana per eccellenza: la panzanella.",
        "Tutte le sere",
        "⭐⭐⭐⭐½ (4.5)"
    ],
    [
        "14/08/2026",
        "16/08/2026",
        "Sagra della Bruschetta",
        "Semproniano",
        "Centro storico, Semproniano",
        "Nel weekend di Ferragosto, Semproniano raddoppia l'offerta affiancando alla panzanella una sagra interamente dedicata alle bruschette rustiche.",
        "Sera",
        "⭐⭐⭐⭐ (4.3)"
    ]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for event in new_events:
        writer.writerow(event)

print(f"Inseriti {len(new_events)} nuovi eventi con successo nel database.")
