import csv

new_events = [
    [
        "01/09/2026",
        "03/09/2026",
        "Festa di Fine Estate e Sagra dell'Orata",
        "Orbetello (Fraz. Albinia)",
        "Giardini di Via Aldi, Albinia",
        "L'ultimo grande appuntamento con i sapori del mare. Specialità marinare, in particolare la pregiata orata locale, e musica dal vivo.",
        "Sera",
        "⭐⭐⭐⭐ (4.1)"
    ],
    [
        "09/09/2026",
        "13/09/2026",
        "Sagra del Cinghiale",
        "Capalbio",
        "Centro storico, Capalbio",
        "Storica manifestazione maremmana incastonata in uno dei borghi più suggestivi della zona. Piatti della tradizione a base di cinghiale accompagnati da eventi e musica.",
        "Tutte le sere",
        "⭐⭐⭐⭐½ (4.6)"
    ],
    [
        "02/10/2026",
        "04/10/2026",
        "Festa dell'Uva",
        "Cinigiano",
        "Centro storico, Cinigiano",
        "Celebrazione dedicata alla vendemmia e alle eccellenze vinicole locali di Cinigiano, territorio noto per la forte vocazione enologica.",
        "Tutto il giorno",
        "⭐⭐⭐⭐ (4.3)"
    ],
    [
        "04/10/2026",
        "12/10/2026",
        "Sagra del Fungo Amiatino",
        "Santa Fiora (Fraz. Bagnolo)",
        "Bagnolo",
        "Imperdibile rassegna dedicata a uno dei prodotti simbolo dei boschi dell'Amiata: il prelibato fungo porcino e le sue declinazioni in cucina.",
        "Fine settimana",
        "⭐⭐⭐⭐½ (4.7)"
    ],
    [
        "17/10/2026",
        "19/10/2026",
        "Sagra della Castagna",
        "Campagnatico (Fraz. Montorsaio)",
        "Montorsaio",
        "Il piccolo borgo si anima per festeggiare la castagna, frutto autunnale per eccellenza, con caldarroste, vino e mercatini.",
        "Tutto il giorno",
        "⭐⭐⭐⭐ (4.2)"
    ],
    [
        "27/11/2026",
        "29/11/2026",
        "Festa dell'Olio",
        "Seggiano",
        "Centro storico, Seggiano",
        "Celebrazione della rinomata 'Olivastra Seggianese', la pregiata cultivar di olivo locale, con degustazioni di olio nuovo, bruschette e visite ai frantoi.",
        "Tutto il giorno",
        "⭐⭐⭐⭐½ (4.6)"
    ]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for event in new_events:
        writer.writerow(event)

print(f"Inseriti {len(new_events)} nuovi eventi autunnali con successo nel database.")
