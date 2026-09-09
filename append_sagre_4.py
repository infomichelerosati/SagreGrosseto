import csv

events = [
    [
        "03/07/2026",
        "12/07/2026",
        "Sagra degli Strozzapreti e dei prodotti tipici maremmani",
        "Roccastrada (Fraz. Sticciano Scalo)",
        "Struttura polivalente in Via Vecchia 12, Sticciano Scalo",
        "30ª edizione della sagra. Nei giorni 3-4-5 e 11-12 luglio ottimi strozzapreti e specialità maremmane.",
        "Solo fine settimana",
        "⭐⭐⭐⭐ (4.2)"
    ],
    [
        "06/07/2026",
        "12/07/2026",
        "Sagra del Pesce",
        "Capalbio (Fraz. La Torba)",
        "La Torba, Capalbio",
        "42ª edizione della storica sagra dedicata ai sapori del mare.",
        "Tutti i giorni",
        "⭐⭐⭐⭐ (4.3)"
    ],
    [
        "11/07/2026",
        "11/07/2026",
        "L'Hamburgerata",
        "Montieri (Fraz. Boccheggiano)",
        "Campo Sportivo Comunale, Boccheggiano",
        "Serata evento dedicata al cibo di strada e ai migliori hamburger.",
        "Singola data",
        "⭐⭐⭐⭐ (4.0)"
    ],
    [
        "11/07/2026",
        "26/07/2026",
        "Festa dello Sport e del Tortello",
        "Grosseto (Fraz. Marina di Grosseto)",
        "Marina di Grosseto",
        "Classico appuntamento estivo che celebra il tortello maremmano a due passi dal mare. Aperta nei fine settimana.",
        "Solo fine settimana",
        "⭐⭐⭐⭐½ (4.5)"
    ],
    [
        "17/07/2026",
        "26/07/2026",
        "Sagra della Pecora e del Maiale",
        "Monterotondo Marittimo",
        "Monterotondo Marittimo",
        "Festa con ricchi menù a base di specialità locali di pecora e maiale.",
        "Tutti i giorni",
        "⭐⭐⭐⭐ (4.2)"
    ]
]

with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for event in events:
        writer.writerow(event)
