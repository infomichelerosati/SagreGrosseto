import csv

event = [
    "23/07/2026",
    "25/07/2026",
    "7ª Festa Country",
    "Castel del Piano",
    "Area Festeggiamenti, Castel del Piano",
    "7ª edizione con atmosfere country. Spettacoli dei Butteri del Marruchetone, Falconieri del Re, cavalli in libertà, balli line dance e dj set. Stand gastronomici aperti dalle 19:30. Ingresso gratuito.",
    "Tutti i giorni",
    "⭐⭐⭐⭐½ (4.5)"
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(event)
