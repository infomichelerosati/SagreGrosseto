import csv
import os
from datetime import datetime

today = datetime.strptime('20/07/2026', '%d/%m/%Y')
active_events = []
past_events = []
header = []

# Read current sagre.csv
with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for row in reader:
        if len(row) < 3:
            active_events.append(row)
            continue
        try:
            end_date_str = row[1].strip()
            end_date = datetime.strptime(end_date_str, '%d/%m/%Y')
            if end_date < today:
                past_events.append(row)
            else:
                active_events.append(row)
        except ValueError:
            # Se la data non è valida o c'è un problema, lo manteniamo in active
            active_events.append(row)

# Write to sagreold.csv (append if exists, create with header if not)
file_exists = os.path.isfile('sagreold.csv')
with open('sagreold.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    if not file_exists and header:
        writer.writerow(header)
    for row in past_events:
        writer.writerow(row)

# Rewrite sagre.csv with only active events
with open('sagre.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    if header:
        writer.writerow(header)
    for row in active_events:
        writer.writerow(row)

print(f"Spostati {len(past_events)} eventi nel file sagreold.csv.")
print(f"Rimasti {len(active_events)} eventi attivi nel file sagre.csv.")
