import csv

new_events = [
    ["24/07/2026", "26/07/2026", "MerCantine in Poggio", "Roccastrada", "Centro Storico, Roccastrada", "Un evento che trasforma il centro storico in un percorso enogastronomico con degustazioni, street food toscano, artigianato e musica dal vivo.", "Solo fine settimana", "⭐⭐⭐⭐ (4.4)"],
    ["01/07/2026", "01/07/2026", "Spettacolo dei Butteri della Maremma", "Grosseto (Fraz. Roselle)", "Roselle", "Appuntamento dedicato alle antiche tradizioni equestri e al mondo dei butteri della Maremma.", "Singola serata", "⭐⭐⭐⭐ (4.5)"]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for event in new_events:
        writer.writerow(event)

print("Added new events!")
