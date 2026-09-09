import csv

new_events = [
    [
        "02/09/2026",
        "08/09/2026",
        "Palio delle Contrade",
        "Castel del Piano",
        "Piazza Garibaldi e Centro Storico, Castel del Piano",
        "[FOLCLORE/PALIO] Storica manifestazione che culmina l'8 settembre con il Palio. La settimana precedente è ricca di eventi popolari: tiro alla fune, corsa degli insaccati, pentolaccia e corteo storico.",
        "Tutti i giorni",
        "⭐⭐⭐⭐⭐ (4.8)"
    ],
    [
        "12/09/2026",
        "13/09/2026",
        "Magico Settembre",
        "Castiglione della Pescaia",
        "Centro, Castiglione della Pescaia",
        "Manifestazione di fine estate dedicata all'artigianato, al vintage, all'hobbistica e alle curiosità nel centro della località balneare.",
        "Tutto il giorno",
        "⭐⭐⭐⭐ (4.1)"
    ],
    [
        "11/09/2026",
        "13/09/2026",
        "Festa delle Cantine",
        "Manciano",
        "Centro Storico, Manciano",
        "Il centro storico si trasforma in un percorso enogastronomico. Le cantine aprono le porte al pubblico per degustazioni di vini locali e piatti tipici (ciaffagnoni, acquacotta, cinghiale).",
        "Dal tardo pomeriggio",
        "⭐⭐⭐⭐⭐ (4.9)"
    ],
    [
        "27/09/2026",
        "28/09/2026",
        "Sagra della Bruschetta e dell'Olio Novo",
        "Castel del Piano (Fraz. Montegiovi)",
        "Montegiovi",
        "Evento enogastronomico di fine settembre che celebra i sapori autunnali della Maremma, con protagonista assoluto il pregiato Olio Extravergine di Oliva del territorio.",
        "Tutti i giorni",
        "⭐⭐⭐⭐½ (4.6)"
    ]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for event in new_events:
        writer.writerow(event)

print(f"Inseriti {len(new_events)} nuovi eventi con successo.")
