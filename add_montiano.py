import csv

event = [
    "10/07/2026",
    "12/07/2026",
    "Sagra Paesana di Montiano",
    "Magliano in Toscana (Fraz. Montiano)",
    "Piazza del Plebiscito, Centro storico di Montiano",
    "Stand aperti dalle 19:30 con piatti della tradizione maremmana, musica dal vivo e spettacoli a sorpresa durante la cena. A cura della Pro Loco Montiano.",
    "Singolo fine settimana",
    "⭐⭐⭐⭐½ (4.5)"
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(event)
