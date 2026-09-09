import csv
from datetime import datetime

new_event = ["10/09/2026", "20/09/2026", "Festa di Santa Lucia", "Grosseto (Quartiere Barbanella)", "Parco Vittore Lino Parri, Barbanella, Grosseto", "58ª edizione della storica festa cittadina. Ristorante 'Simone Pellegrini' aperto dalle 19:00, stand gastronomici, fiera di beneficenza, tombola serale e grandi concerti live (incluso Eugenio Finardi).", "Tutti i giorni", "⭐⭐⭐⭐½ (4.7)"]

file_path = 'sagre.csv'
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)

# Append new event
data.append(new_event)

# Clean empty rows
data = [row for row in data if any(row)]

# Function to parse date for sorting.
def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), "%d/%m/%Y")
    except ValueError:
        return datetime.max 

# Sort data by Data Inizio
data.sort(key=lambda x: parse_date(x[0]))

# Write back
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("Added Festa di Santa Lucia to sagre.csv and sorted chronologically.")
