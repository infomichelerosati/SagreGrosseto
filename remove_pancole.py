import csv

lines = []
with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 2 and "Sagra della Lasagna di Pancole" in row[2]:
            continue # skip it
        lines.append(row)

with open('sagre.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in lines:
        writer.writerow(row)
