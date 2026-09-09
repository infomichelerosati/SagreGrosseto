import csv

event = [
    "10/07/2026",
    "19/07/2026",
    "Sagra della Panzanella",
    "Orbetello (Fraz. San Donato)",
    "Impianti Sportivi di San Donato, Orbetello",
    "27ª edizione imperdibile! Dalle 19:30 stand aperti per gustare la celebre panzanella fresca, accompagnata da fragranti tortelli maremmani, gnocchi e ottima carne alla brace.",
    "Tutti i giorni",
    "⭐⭐⭐⭐½ (4.5)"
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(event)
