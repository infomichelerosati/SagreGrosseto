# -*- coding: utf-8 -*-
import csv

new_events = [
    ["23/07/2026", "13/08/2026", "Follonica Summer Nights", "Follonica", "Parco Centrale, Follonica", "Grande festival estivo con concerti di artisti di rilevanza nazionale, spettacoli di cabaret e musical all'aperto.", "Date specifiche dei concerti", "⭐⭐⭐⭐⭐ (4.8)"],
    ["14/08/2026", "16/08/2026", "Palio Marinaro dell'Argentario", "Monte Argentario (Fraz. Porto Santo Stefano)", "Porto e lungomare di Porto Santo Stefano", "Celebrazione e regata storica del 15 agosto, con sfilate, eventi e le tradizionali sfide remiere tra i rioni.", "15 Agosto (gara principale)", "⭐⭐⭐⭐⭐ (4.9)"]
]

with open("sagre.csv", mode="a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for ev in new_events:
        writer.writerow(ev)
