import csv

def add_event():
    with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "10/07/2026",
            "24/07/2026",
            "Le Notti dell'Archeologia",
            "Pitigliano",
            "Museo archeologico A. Manzi e E. Pellegrini, Pitigliano",
            "Rassegna con visite guidate, incontri e letture dedicate all'archeologia etrusca. Il tema di quest'anno è 'Archeologia che unisce un mondo diviso'. Include visite guidate (es. 11 luglio ore 21:30) ed eventi con degustazioni (17 luglio ore 18:00).",
            "",
            "⭐⭐⭐⭐ (4.3)"
        ])

if __name__ == '__main__':
    add_event()
