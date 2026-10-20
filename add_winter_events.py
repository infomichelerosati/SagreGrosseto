import csv
import sys
from datetime import datetime

file_path = 'sagre.csv'

new_events = [
    {
        "Data Inizio": "05/12/2026",
        "Data Fine": "24/12/2026",
        "Nome Evento": "Natale a Massa Marittima e Mercatini nel Chiostro",
        "Comune / Frazione": "Massa Marittima",
        "Luogo Esatto": "Chiostro di Sant'Agostino, Piazza Garibaldi e centro storico, Massa Marittima",
        "Descrizione dell'Evento": "Rassegna natalizia nel cuore delle Colline Metallifere. Il suggestivo Chiostro di Sant'Agostino ospita i mercatini di Natale con artigianato, prodotti tipici locali e degustazioni di vino Monteregio DOC, caldarroste fumanti e dolci toscani (panforte, cavallucci, ricciarelli). In Piazza Garibaldi pista di pattinaggio sul ghiaccio e Casina di Babbo Natale.",
        "Giorni Effettivi": "Tutti i weekend e festivi (dalle 10:00 alle 20:00)",
        "Valutazione": "⭐⭐⭐⭐½ (4.6)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🎄 Mercatini nel Chiostro & Tradizioni</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Bancarelle d\'artigianato locale, idee regalo e addobbi all\'interno del magnifico Chiostro di Sant\'Agostino a cura del Terziere di Cittanuova.</li><li>Stand gastronomici con caldarroste, vin brulé caldo, dolci tipici toscani (ricciarelli, panforte e cavallucci) e degustazioni di vino Monteregio DOC.</li><li>Apertura tutti i fine settimana di dicembre e nei giorni festivi dalle ore 10:00 alle 20:00.</li></ul><p class="mb-2 text-maremma-700"><strong>⛸️ Attrazioni in Piazza Garibaldi</strong></p><ul class="list-disc pl-5 space-y-1"><li>Pista di pattinaggio sul ghiaccio all\'aperto ai piedi della maestosa Cattedrale di San Cerbone.</li><li>La Casina di Babbo Natale con l\'ufficio postale per le letterine dei bambini e animazione pomeridiana.</li></ul>'
    },
    {
        "Data Inizio": "05/12/2026",
        "Data Fine": "06/01/2027",
        "Nome Evento": "Natale di Luce ad Arcidosso",
        "Comune / Frazione": "Arcidosso",
        "Luogo Esatto": "Piazza Indipendenza, Corso Toscana e centro storico, Arcidosso",
        "Descrizione dell'Evento": "La grande kermesse natalizia del Monte Amiata. Mercatini nelle caratteristiche casette in legno con eccellenze agroalimentari locali (castagne e farina dolce amiatina, necci caldi con ricotta fresca, vin brulé speziato, salumi di cinta senese e pecorini toscani), Villaggio di Babbo Natale, grande pista di pattinaggio sul ghiaccio e rassegna di presepi artistici.",
        "Giorni Effettivi": "Tutti i fine settimana, festivi e periodo natalizio continuo",
        "Valutazione": "⭐⭐⭐⭐⭐ (4.8)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🌰 Sapori Amiatini & Casette di Legno</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Mercatino di Natale in Corso Toscana con prodotti enogastronomici a km 0 del Monte Amiata: castagnaccio, necci con ricotta, caldarroste, formaggi pecorini e salumi artigianali.</li><li>Vin brulé speziato e dolci di castagne preparati sul momento.</li><li>Stand aperti tutti i sabati, domeniche e giorni festivi (continuativo durante le vacanze scolastiche).</li></ul><p class="mb-2 text-maremma-700"><strong>✨ Spettacoli & Famiglie</strong></p><ul class="list-disc pl-5 space-y-1"><li>Grande pista di pattinaggio su ghiaccio coperta in Piazza Indipendenza.</li><li>Il suggestivo Villaggio di Babbo Natale con laboratori e giochi per bambini.</li><li>Percorso diffuso dei Presepi artistici nelle chiese e nelle antiche cantine del borgo medievale.</li></ul>'
    },
    {
        "Data Inizio": "26/12/2026",
        "Data Fine": "06/01/2027",
        "Nome Evento": "Presepe Vivente di Pitigliano",
        "Comune / Frazione": "Pitigliano",
        "Luogo Esatto": "Rione storico Capisotto e vie scavate nel tufo, Pitigliano",
        "Descrizione dell'Evento": "Una delle più suggestive rappresentazioni storiche e religiose della Toscana, ambientata nello scenario rupestre dell'antico rione Capisotto. Oltre 80 figuranti in costume animano vicoli, cantine e grotte scavate nel tufo rievocando gli antichi mestieri artigiani, accompagnati da punti ristoro con cibi poveri della tradizione maremmana, formaggi, bruschette all'olio nuovo e vino caldo speziato.",
        "Giorni Effettivi": "26 e 30 Dicembre, 6 Gennaio (dalle 16:30 alle 19:30)",
        "Valutazione": "⭐⭐⭐⭐⭐ (4.9)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🕯️ La Natività nel Tufo</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Rievocazione storica tra le antiche vie tufacee e le cantine rupestri del rione Capisotto (partenza da Piazza San Gregorio).</li><li>Oltre 80 figuranti in costumi d\'epoca: fabbri, falegnami, pastori, fornai e tessitrici al lavoro lungo il percorso.</li><li>Rappresentazioni nei pomeriggi del 26 dicembre (Santo Stefano), 30 dicembre e 6 gennaio (Epifania, con l\'arrivo dei Re Magi a cavallo) dalle 16:30 alle 19:30.</li></ul><p class="mb-2 text-maremma-700"><strong>🍷 Degustazioni Tradizionali</strong></p><ul class="list-disc pl-5 space-y-1"><li>Punti ristoro allestiti nelle grotte con pane casereccio toscano e olio nuovo appena franto, pecorino maremmano, frittelle calde, sfratto di Pitigliano e vino caldo speziato.</li></ul>'
    },
    {
        "Data Inizio": "26/12/2026",
        "Data Fine": "06/01/2027",
        "Nome Evento": "Presepe Vivente di Castiglione della Pescaia",
        "Comune / Frazione": "Castiglione della Pescaia",
        "Luogo Esatto": "Borgo medievale e salita al Castello, Castiglione della Pescaia",
        "Descrizione dell'Evento": "Rievocazione storica della Natività che si inerpica lungo i vicoli acciottolati del borgo fortificato affacciato sul mare fino alla Rocca. Scene di vita quotidiana e antichi mestieri contadini e marinari con figuranti in costume, botteghe con degustazione di dolci tradizionali toscani, frittelle calde, ciambelline e vin brulé.",
        "Giorni Effettivi": "26 Dicembre e 6 Gennaio (pomeriggio dalle 16:00 alle 19:00)",
        "Valutazione": "⭐⭐⭐⭐½ (4.5)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🏰 Presepe nel Borgo Medievale</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Rappresentazione storica che si sviluppa lungo la salita panoramica verso il Castello medievale di Castiglione della Pescaia.</li><li>Scene di antichi mestieri marinari e rurali maremmani con figuranti in costume d\'epoca.</li><li>Repliche pomeridiane il 26 Dicembre e il 6 Gennaio (con il corteo dei Re Magi) dalle ore 16:00.</li></ul><p class="mb-2 text-maremma-700"><strong>🍩 Sapori della Festa</strong></p><ul class="list-disc pl-5 space-y-1"><li>Bancarelle e punti ristoro con frittelle di riso dolci, ciambelle all\'anice, dolci toscani natalizi e vin brulé caldo servito all\'arrivo alla terrazza panoramica.</li></ul>'
    },
    {
        "Data Inizio": "17/01/2027",
        "Data Fine": "17/01/2027",
        "Nome Evento": "Festa di Sant'Antonio Abate dei Butteri",
        "Comune / Frazione": "Grosseto (Fraz. Alberese)",
        "Luogo Esatto": "Centro aziendale e sagrato della Chiesa, Frazione Alberese (Grosseto)",
        "Descrizione dell'Evento": "Celebrazione identitaria dell'anima buttera della Maremma alle porte del Parco Naturale. Solenne benedizione degli animali domestici e dei magnifici cavalli e vacche maremmane, sfilata e carosello dei butteri in sella con bardature tradizionali, seguita da stand gastronomici con salsiccia maremmana alla brace, bruschette calde con l'olio nuovo appena franto, dolci tipici e vino rosso locale.",
        "Giorni Effettivi": "Domenica 17 Gennaio (dalle 09:30 al pomeriggio)",
        "Valutazione": "⭐⭐⭐⭐⭐ (4.8)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🐎 Tradizione Equestre & Butteri</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Ore 09:30: Raduno dei butteri a cavallo con bardatura tradizionale maremmana e arrivo degli allevatori con animali.</li><li>Ore 11:00: Santa Messa solenne e tradizionale Benedizione degli Animali (cavalli, cani, vacche maremmane) sul sagrato della chiesa di Alberese.</li><li>A seguire spettacolare sfilata ed esibizione dei butteri nel piazzale del centro aziendale.</li></ul><p class="mb-2 text-maremma-700"><strong>🔥 Brace & Gastronomia Contadina</strong></p><ul class="list-disc pl-5 space-y-1"><li>Dalle ore 12:30 grande grigliata conviviale all\'aperto: salsicce toscane, rigatino e carni maremmane alla brace.</li><li>Bruschette all\'olio nuovo d\'oliva appena franto, dolci tipici casalinghi e vino Morellino e Maremma DOC.</li></ul>'
    },
    {
        "Data Inizio": "07/02/2027",
        "Data Fine": "16/02/2027",
        "Nome Evento": "Carnevale di Pitigliano",
        "Comune / Frazione": "Pitigliano",
        "Luogo Esatto": "Piazza Nenni, Piazza della Repubblica e centro storico, Pitigliano",
        "Descrizione dell'Evento": "Sentita festa popolare che anima le monumentali vie del borgo del tufo. Grandi sfilate di carri allegorici artigianali e cortei mascherati, musica dal vivo e chioschi gastronomici dedicati ai dolci della tradizione di carnevale (cenci fritti spolverati di zucchero a velo, frittelle di riso dolci di San Giuseppe e castagnole calde), accompagnati da brindisi con i rinomati vini bianchi e rossi delle cantine locali.",
        "Giorni Effettivi": "Domeniche di febbraio (7 e 14) e Martedì Grasso (16 febbraio)",
        "Valutazione": "⭐⭐⭐⭐½ (4.6)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🎭 Le Parate dei Carri sul Tufo</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Domenica 7 e 14 Febbraio dalle ore 14:30: Grande sfilata dei carri allegorici e gruppi mascherati con partenza da Piazza Nenni fino a Piazza della Repubblica.</li><li>Martedì Grasso 16 Febbraio (pomeriggio e sera): Sfilata conclusiva in maschera, proclamazione della maschera più originale, premiazione e festa finale.</li><li>Lancio di coriandoli, musica con DJ set e spettacoli per famiglie.</li></ul><p class="mb-2 text-maremma-700"><strong>🍩 I Dolci di Carnevale</strong></p><ul class="list-disc pl-5 space-y-1"><li>Stand e chioschi aperti con le specialità dolciarie tipiche toscane: cenci fritti caldi, frittelle di riso dolci di San Giuseppe, castagnole e bomboloni.</li><li>Degustazione di vini locali delle cantine di Pitigliano.</li></ul>'
    }
]

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

existing_names = [r[2].strip().lower() for r in rows if len(r) >= 3]

added = 0
for ev in new_events:
    name_norm = ev["Nome Evento"].strip().lower()
    if name_norm in existing_names:
        print(f"GIA PRESENTE: {ev['Nome Evento']}")
        continue
    row = [
        ev["Data Inizio"],
        ev["Data Fine"],
        ev["Nome Evento"],
        ev["Comune / Frazione"],
        ev["Luogo Esatto"],
        ev["Descrizione dell'Evento"],
        ev["Giorni Effettivi"],
        ev["Valutazione"],
        ev["Programma Dettagliato"]
    ]
    rows.append(row)
    added += 1
    print(f"AGGIUNTO: {ev['Nome Evento']}")

def parse_date(d_str):
    try:
        return datetime.strptime(d_str.strip(), '%d/%m/%Y')
    except Exception:
        return datetime.max

rows.sort(key=lambda r: (parse_date(r[0]), parse_date(r[1]) if len(r) > 1 else datetime.max))

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"\nOperazione completata: inseriti {added} nuovi eventi.")
print(f"Totale righe ora in {file_path}: {len(rows)}.")
