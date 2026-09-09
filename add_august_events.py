import csv

new_events = [
    [
        "27/08/2026",
        "30/08/2026",
        "Palio delle Botti",
        "Manciano",
        "Centro Storico, Manciano",
        "[FOLCLORE/PALIO] I sei rioni si sfidano in una spettacolare corsa spingendo botti piene d'acqua per le vie del borgo. Corteo storico, sfide e stand enogastronomici.",
        "Tutti i giorni",
        "⭐⭐⭐⭐ (4.4)"
    ],
    [
        "23/08/2026",
        "23/08/2026",
        "Palio Marinaro dell'Assunta (70ª edizione)",
        "Castiglione della Pescaia",
        "Porto canale (partenza dal Faro Rosso)",
        "[FOLCLORE/PALIO] 70ª edizione senior della tradizionale regata storica tra i cinque rioni del paese a bordo delle tipiche imbarcazioni a remi.",
        "Gara il 23 Agosto",
        "⭐⭐⭐⭐⭐ (4.9)"
    ],
    [
        "08/08/2026",
        "08/08/2026",
        "Notte Rosa",
        "Manciano (Fraz. Saturnia)",
        "Centro Storico, Saturnia",
        "Serata di festa nel cuore della cittadina termale, con il borgo che si anima di musica, eventi, intrattenimento per le vie e tanta allegria.",
        "Dalle 20:00",
        "⭐⭐⭐⭐ (4.3)"
    ],
    [
        "12/08/2026",
        "12/08/2026",
        "Numera Stellas - La Notte delle Stelle Cadenti",
        "Manciano",
        "Ritrovo in paese (Manciano)",
        "Passeggiata ed escursione serale speciale organizzata per l'osservazione del cielo notturno, sfruttando il bassissimo inquinamento luminoso delle colline.",
        "Ritrovo ore 20:30",
        "⭐⭐⭐⭐ (4.1)"
    ]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for event in new_events:
        writer.writerow(event)

print(f"Inseriti {len(new_events)} nuovi eventi con successo.")
