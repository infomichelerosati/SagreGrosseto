import csv

filtered_events = []
removed_count = 0

with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 3:
            name = row[2].lower()
            if 'sagra a buriano' in name or 'sarde e calamari in festa' in name:
                removed_count += 1
                continue
        filtered_events.append(row)

with open('sagre.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in filtered_events:
        writer.writerow(row)

print(f"Rimossi {removed_count} eventi invalidi dal file sagre.csv.")
