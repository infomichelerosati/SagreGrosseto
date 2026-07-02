# -*- coding: utf-8 -*-
import csv

new_events = [
    ["02/07/2026", "05/07/2026", "Sagra del Maiale", "Orbetello (Loc. San Donato)", "Campo Sportivo San Donato", "Appuntamento storico (25a edizione) dedicato alle grigliate di carne suina e alla cucina locale.", "Tutti i giorni", "⭐⭐⭐⭐ (4.4)"],
    ["03/07/2026", "02/08/2026", "Festa dello Sport e del Cinghiale alla Cacciatora", "Grosseto (Fraz. Rispescia)", "Impianti Sportivi di Rispescia", "Occasione per gustare il tipico cinghiale in umido nel cuore del Parco Regionale della Maremma. Organizzata dalla squadra locale.", "Ogni venerdì, sabato e domenica", "⭐⭐⭐⭐⭐ (4.6)"]
]

with open("sagre.csv", mode="a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for ev in new_events:
        writer.writerow(ev)
