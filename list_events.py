# -*- coding: utf-8 -*-
import csv
with open("sagre.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for i, row in enumerate(reader):
        print(f"[{i+2}] {row[0]}-{row[1]} : {row[2]} ({row[3]})")
