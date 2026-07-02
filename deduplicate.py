# -*- coding: utf-8 -*-
import csv
import sys

input_file = "sagre.csv"
output_file = "sagre_dedup.csv"

seen = set()
duplicates = []

with open(input_file, mode="r", encoding="utf-8") as infile, open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)
    writer.writerow(header)
    
    for row in reader:
        if not row:
            continue
        # Use Nome Evento as unique key, normalized
        name = row[2].strip().lower()
        if name in seen:
            duplicates.append(row[2])
            continue
        seen.add(name)
        writer.writerow(row)

for d in duplicates:
    print("Duplicate removed:", d)
