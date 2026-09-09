import csv

def add_event():
    with open('sagre.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "05/07/2026",
            "07/07/2026",
            "CINEMURA - Cinema all'aperto",
            "Grosseto",
            "Il Giardino degli Arcieri, Piazza Amos Nannini 12, Grosseto",
            "Rassegna di cinema all'aperto. 5/7: 19:00 Incontro arte inclusiva, 21:00 I Goonies, giropizza. 6/7: 21:00 Selezione Cineteca di Bologna. 7/7: 21:00 Documentari e dibattito su spazi condivisi, presentazione Primo Binario Film Lab. Dalle 19 aperitivo, ingresso a offerta libera.",
            "",
            "⭐⭐⭐⭐½ (4.5)"
        ])

if __name__ == '__main__':
    add_event()
