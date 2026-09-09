# -*- coding: utf-8 -*-
import csv

new_events = [
    [
        "05/08/2026", "09/08/2026", "Festambiente (Ecofestival Nazionale)", "Grosseto (Fraz. Rispescia)", "Località Enaoli",
        "[ECOFESTIVAL] Festival nazionale di Legambiente. Cinque giornate che uniscono concerti di grandi artisti (es. Modena City Ramblers, The Zen Circus), cinema, dibattiti sull'ambiente, e gastronomia biologica.",
        "Tutti i giorni", "⭐⭐⭐⭐ (4.5)"
    ],
    [
        "08/07/2026", "12/07/2026", "Sincronie Summer Festival", "Massa Marittima", "Centro storico",
        "[MUSICA] Prestigiosa rassegna musicale estiva che ospita concerti di artisti e solisti di fama internazionale nella splendida cornice del borgo medievale.",
        "Tutti i giorni", "⭐⭐⭐⭐ (4.5)"
    ],
    [
        "31/07/2026", "31/08/2026", "Festival del Teatro Antico", "Grosseto (Parco Archeologico di Roselle)", "Anfiteatro Romano di Roselle",
        "[TEATRO] Rassegna di spettacoli teatrali classici e moderni messi in scena all'interno del suggestivo anfiteatro romano di Roselle per tutto il mese di agosto.",
        "Date variabili", "⭐⭐⭐⭐ (4.5)"
    ],
    [
        "09/08/2026", "10/08/2026", "San Lorenzo e Premio Grifone d'Oro", "Grosseto", "Centro storico",
        "[FESTA STORICA/PATRONALE] Tradizionale processione del 9 agosto con i Butteri a cavallo, seguita il 10 agosto (giorno del Patrono) dalla consegna del prestigioso Premio Grifone d'Oro.",
        "9 e 10 agosto", "⭐⭐⭐⭐ (4.5)"
    ],
    [
        "14/08/2026", "14/08/2026", "Palio dei Ciuchi", "Roccastrada (Fraz. Roccatederighi)", "Antiche contrade del borgo",
        "[FOLCLORE/PALIO] Storica corsa a dorso d'asino ('ciuchi') tra le antiche contrade del borgo, anticipata da un pittoresco corteo storico in costumi del Quattrocento.",
        "Singola giornata", "⭐⭐⭐⭐ (4.5)"
    ],
    [
        "25/07/2026", "15/08/2026", "Amiata Music Festival", "Cinigiano (Fraz. Poggi del Sasso)", "Forum Bertarelli",
        "[MUSICA CLASSICA] Eventi musicali di altissimo profilo, tra cui il Gala Lirico, recital internazionali e concerti sinfonici nelle tenute della Maremma.",
        "Date variabili (25 luglio, 9 e 15 agosto)", "⭐⭐⭐⭐ (4.5)"
    ],
    [
        "01/07/2026", "06/09/2026", "Mostra Il tempo del realismo", "Grosseto", "Polo culturale Le Clarisse",
        "[MOSTRA D'ARTE] Grande esposizione d'arte che ospita capolavori del realismo (Guttuso, Levi, Treccani) affiancati dalle opere degli artisti maremmani.",
        "Tutti i giorni (lunedì chiuso)", "⭐⭐⭐⭐ (4.5)"
    ]
]

with open("sagre.csv", mode="a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for ev in new_events:
        writer.writerow(ev)

print("Added 7 events successfully!")
