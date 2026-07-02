# -*- coding: utf-8 -*-
import csv

new_events = [
    ["11/07/2026", "13/07/2026", "Manciano Street Music Festival", "Manciano", "Vie del borgo storico, Manciano", "Festival musicale itinerante per le vie del centro, con artisti e street band internazionali e stand gastronomici.", "Tutti i giorni", "⭐⭐⭐⭐⭐ (4.8)"],
    ["01/08/2026", "02/08/2026", "Festa del Contadino", "Pitigliano", "Zona rurale, Pitigliano", "Rievocazione delle tradizioni rurali maremmane con sfilata di trattori d''epoca, giochi popolari e ricca cena conviviale.", "Solo weekend", "⭐⭐⭐⭐ (4.4)"],
    ["08/08/2026", "09/08/2026", "Calici di Stelle", "Pitigliano", "Centro storico, Pitigliano", "Serata dedicata alle degustazioni dei grandi vini locali (Bianco di Pitigliano DOC) e prodotti tipici con musica sotto le stelle.", "Tutti i giorni", "⭐⭐⭐⭐⭐ (4.7)"]
]

with open("sagre.csv", mode="a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for ev in new_events:
        writer.writerow(ev)
