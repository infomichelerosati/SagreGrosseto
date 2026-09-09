import csv

lines = []
with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 2 and "Sagra del Pesce a La Torba" in row[2]:
            row[0] = "06/07/2026"
            row[1] = "12/07/2026"
            row[5] = "42ª edizione. Ricette di pesce tradizionali (insalata di mare, seppie e ceci, zuppa, frittura e grigliata). Stand dalle 19:30 al Circolo La Torbiera con uso di stoviglie biodegradabili."
        lines.append(row)

with open('sagre.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in lines:
        writer.writerow(row)
