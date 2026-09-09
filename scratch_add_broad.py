import csv
from datetime import datetime

new_events = [
    ["12/09/2026", "13/09/2026", "A spasso nel Medioevo - Sulle orme del Grifone", "Grosseto", "Centro Storico e Cassero Senese, Grosseto", "Grande manifestazione di rievocazione storica. Mercatino medievale, artigianato, living history, spettacoli in costume e stand gastronomici a tema.", "Sabato e Domenica", "⭐⭐⭐⭐½ (4.5)"],
    ["01/09/2026", "25/10/2026", "Cantine Aperte in Vendemmia", "Varie località (Provincia di Grosseto)", "Aziende vitivinicole della Maremma", "Iniziativa diffusa in tutta la provincia. Le cantine aprono le porte ai visitatori per far vivere l'esperienza della vendemmia, con degustazioni di mosto e vini locali.", "Tutti i weekend", "⭐⭐⭐⭐½ (4.6)"]
]

file_path = 'sagre.csv'
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)

# Append new events
data.extend(new_events)

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

print(f"Added {len(new_events)} non-sagra events and sorted chronologically.")
