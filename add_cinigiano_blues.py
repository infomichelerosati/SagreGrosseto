# -*- coding: utf-8 -*-
import csv

new_event = [
    "10/07/2026", 
    "12/07/2026", 
    "Cinigiano Blues Festival", 
    "Cinigiano", 
    "Castello di Porrona, Cinigiano", 
    "Tre giorni di musica blues internazionale a ingresso gratuito, mercatini e area ristoro attiva dalle ore 19. Start live 21.30 con Michele Biondi Band, Giuseppe Scarpato Power Trio e Irene Fornaciari & The Groove Aviators. Info Whatsapp: 334 655 2360.", 
    "Tutti i giorni", 
    "⭐⭐⭐⭐⭐ (5.0)"
]

with open("sagre.csv", mode="a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_event)

print("Added successfully!")
