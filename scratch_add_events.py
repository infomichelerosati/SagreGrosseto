import csv
from datetime import datetime

new_events = [
    ["08/11/2026", "09/11/2026", "Festa del Buco Unto", "Civitella Paganico (Fraz. Civitella Marittima)", "Centro Storico e Cantine, Civitella Marittima", "Storica festa dedicata all'olio nuovo e al vino novello. Cantine aperte, pici al sugo di vino novello, bruschette, musica dal vivo e mercatini artigianali nel borgo medievale.", "Sabato e Domenica", "⭐⭐⭐⭐½ (4.6)"],
    ["08/11/2026", "09/11/2026", "Festa dell'Olio Novo", "Manciano (Fraz. Marsiliana)", "Centro Storico, Marsiliana", "Appuntamento autunnale dedicato alla celebrazione dell'olio extravergine d'oliva nuovo locale. Degustazioni di bruschette, piatti della tradizione contadina e intrattenimento.", "Sabato e Domenica", "⭐⭐⭐⭐ (4.3)"]
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

print(f"Added {len(new_events)} new late autumn events and sorted chronologically.")
