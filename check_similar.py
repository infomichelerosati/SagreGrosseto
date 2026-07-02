# -*- coding: utf-8 -*-
import csv

with open("sagre.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

from collections import defaultdict
comune_map = defaultdict(list)

for r in rows:
    comune_map[r["Comune / Frazione"]].append(r["Nome Evento"])

for c, events in comune_map.items():
    if len(events) > 1:
        print(f"Comune: {c}")
        for e in events:
            print(f"  - {e}")
