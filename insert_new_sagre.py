import csv
import sys
from datetime import datetime

file_path = 'sagre.csv'

new_events = [
    {
        "Data Inizio": "25/09/2026",
        "Data Fine": "27/09/2026",
        "Nome Evento": "Sasso in Festa",
        "Comune / Frazione": "Cinigiano (Fraz. Sasso d'Ombrone)",
        "Luogo Esatto": "Parco Bellacosta e centro storico, Sasso d'Ombrone",
        "Descrizione dell'Evento": "Rassegna paesana e culturale che trasforma il borgo medievale in una galleria d'arte a cielo aperto. Ristorante gastronomico al Parco Bellacosta con piatti della tradizione maremmana, cantine aperte con degustazione di vini Montecucco D.O.C., mostre fotografiche sulla memoria contadina, mercatino artigianale e serate di musica dal vivo con DJ set.",
        "Giorni Effettivi": "Weekend (Venerdì a cena, Sabato e Domenica pranzo e cena)",
        "Valutazione": "⭐⭐⭐⭐½ (4.5)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🍽️ Stand Gastronomici & Degustazioni</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Ristorante gastronomico allestito al Parco Bellacosta con piatti della tradizione maremmana (tortelli, carni alla brace, specialità paesane).</li><li>Apertura delle caratteristiche cantine del centro storico con degustazioni del celebre vino Montecucco D.O.C.</li><li>Stand attivi venerdì e sabato a cena (dalle 19:30), domenica sia a pranzo (dalle 12:30) che a cena.</li></ul><p class="mb-2 text-maremma-700"><strong>🎨 Cultura, Mostre & Spettacoli</strong></p><ul class="list-disc pl-5 space-y-1"><li><strong>Venerdì:</strong> Apertura della festa, mostre d\'arte contemporanea tra i vicoli del borgo medievale e live music serale con DJ set.</li><li><strong>Sabato:</strong> Mostra fotografica sulla memoria contadina, passeggiata panoramica pomeridiana lungo la valle dell\'Ombrone e grande concerto serale al parco.</li><li><strong>Domenica:</strong> Dalla mattina mercatino dell\'artigianato e dell\'antiquariato, giochi popolari per bambini nel pomeriggio e musica dal vivo di chiusura.</li></ul>'
    },
    {
        "Data Inizio": "10/10/2026",
        "Data Fine": "10/10/2026",
        "Nome Evento": "Festa di San Cerbone e Sfida della Balestra",
        "Comune / Frazione": "Massa Marittima",
        "Luogo Esatto": "Piazza Garibaldi e Cattedrale di San Cerbone, Massa Marittima",
        "Descrizione dell'Evento": "[FOLCLORE/PATRONO] Solenne celebrazione del Santo Patrono delle Colline Metallifere. Spettacolare corteo storico con oltre cento figuranti in costumi medievali, sbandieratori e musici della Società dei Terzieri Massetani, cerimonia dell'offerta del cero e del censo al Vescovo in Cattedrale e tradizionale gara straordinaria di tiro con la balestra sul sagrato del Duomo contro il bersaglio 'corniolo', accompagnata da stand gastronomici e sapori tipici del territorio.",
        "Giorni Effettivi": "Singola giornata (Sabato 10 Ottobre)",
        "Valutazione": "⭐⭐⭐⭐⭐ (4.8)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🏹 Solenni Celebrazioni & Torneo della Balestra</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li><strong>Ore 10:30:</strong> Solenne Messa Pontificale nella maestosa Cattedrale di San Cerbone con le autorità cittadine e i rappresentanti dei Terzieri.</li><li><strong>Ore 15:30:</strong> Partenza del maestoso Corteo Storico medievale con oltre cento figuranti in costumi del Trecento, musici e sbandieratori della Società dei Terzieri Massetani.</li><li><strong>Ore 16:30:</strong> Solenne cerimonia medievale dell\'Offerta del Cero e del Censo al Vescovo.</li><li><strong>Ore 17:15:</strong> Straordinaria ed emozionante sfida di tiro con la balestra antica all\'italiana sul sagrato del Duomo: i migliori balestrieri di Borgo, Cittanuova e Cittavecchia si contendono la vittoria centrando il "corniolo".</li></ul><p class="mb-2 text-maremma-700"><strong>🍷 Sapori d\'Autunno nel Borgo</strong></p><ul class="list-disc pl-5 space-y-1"><li>Dalle ore 12:00 e per tutto il pomeriggio: Punti di ristoro in piazza con caldarroste fumanti, necci con ricotta, schiaccia con l\'uva e degustazioni dei rinomati vini Monteregio di Massa Marittima.</li></ul>'
    },
    {
        "Data Inizio": "23/10/2026",
        "Data Fine": "25/10/2026",
        "Nome Evento": "Festa della Castagna di Sassofortino",
        "Comune / Frazione": "Roccastrada (Fraz. Sassofortino)",
        "Luogo Esatto": "Parco comunale della Fonte di Vandro e vie del paese, Sassofortino",
        "Descrizione dell'Evento": "Tradizionale e partecipatissimo appuntamento autunnale organizzato dalla Pro Loco Sasso&Forte nel fresco dei secolari castagneti. Stand gastronomici con piatti a tema: caldarroste fumanti, castagnaccio, necci con ricotta fresca, ma anche tortelli maremmani al ragù, spezzatino di cinghiale e vin brulé, con mercatino d'artigianato locale e intrattenimento musicale.",
        "Giorni Effettivi": "Solo fine settimana (Venerdì sera, Sabato e Domenica)",
        "Valutazione": "⭐⭐⭐⭐½ (4.5)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🌰 Stand Gastronomici & Sapori del Bosco</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Ristorante al coperto presso il fresco Parco comunale della Fonte di Vandro con menù autunnale: tortelli maremmani al ragù, spezzatino di cinghiale alla cacciatora, polenta e salsicce alla brace.</li><li>Leccornie a base di castagne locali: caldarroste preparate sulle grandi padelle forate, fragrante castagnaccio toscano, necci caldi con ricotta fresca e vin brulé speziato.</li><li>Orari apertura: Venerdì a cena dalle 19:30; Sabato cena dalle 19:00; Domenica pranzo dalle 12:30 e cena dalle 19:00.</li></ul><p class="mb-2 text-maremma-700"><strong>🎵 Mercatini & Intrattenimento</strong></p><ul class="list-disc pl-5 space-y-1"><li><strong>Sabato pomeriggio:</strong> Apertura del mercatino di prodotti tipici e artigianato locale nel parco, animazione per bambini e spettacoli musicali serali.</li><li><strong>Domenica:</strong> Escursioni e passeggiate guidate tra i castagneti secolari della Fonte di Vandro, musica itinerante con stornellatori toscani e ballo all\'aperto.</li></ul>'
    },
    {
        "Data Inizio": "01/11/2026",
        "Data Fine": "15/11/2026",
        "Nome Evento": "Cantine Aperte a San Martino",
        "Comune / Frazione": "Varie località (Provincia di Grosseto)",
        "Luogo Esatto": "Aziende vitivinicole aderenti della Maremma Grossetana",
        "Descrizione dell'Evento": "Iniziativa promossa dal Movimento Turismo del Vino per celebrare l'antico rito del vino novello ('per San Martino ogni mosto diventa vino'). Le storiche tenute e cantine della Maremma aprono le porte per visite ai vigneti autunnali, assaggi di vino novello direttamente dalla botte, degustazioni di bruschette all'olio nuovo appena franto, caldarroste e prodotti tipici a km zero.",
        "Giorni Effettivi": "Fine settimana (1-15 Novembre)",
        "Valutazione": "⭐⭐⭐⭐½ (4.6)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🍷 L\'Enoturismo d\'Autunno in Maremma</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Iniziativa ufficiale promossa dal Movimento Turismo del Vino Toscana nelle storiche tenute e cantine della provincia di Grosseto.</li><li>Dalle ore 10:00 alle 18:00 (tutti i weekend dal 1° al 15 Novembre): Accoglienza degli enoturisti con visite guidate alle cantine e passeggiate tra i vigneti dalle calde sfumature autunnali.</li><li>Degustazione speciale del Vino Novello appena spillato direttamente dai tini e dalle botti, secondo l\'antico adagio contadino: <em>"A San Martino ogni mosto diventa vino"</em>.</li></ul><p class="mb-2 text-maremma-700"><strong>🥖 Abbinamenti & Prodotti Tipici</strong></p><ul class="list-disc pl-5 space-y-1"><li>Fettunta maremmana con il pregiato Olio Extravergine d\'Oliva nuovo appena franto.</li><li>Caldarroste fumanti, castagnaccio casereccio e taglieri con pecorino toscano D.O.P. e salumi di cinta senese.</li><li><em>Nota: È consigliata la prenotazione diretta presso le singole cantine aderenti.</em></li></ul>'
    },
    {
        "Data Inizio": "07/02/2027",
        "Data Fine": "28/02/2027",
        "Nome Evento": "Carnevaletto da 3 Soldi (56ª Edizione)",
        "Comune / Frazione": "Orbetello",
        "Luogo Esatto": "Corso Italia e centro storico, Orbetello",
        "Descrizione dell'Evento": "[CARNEVALE/FOLCLORE] Lo storico carnevale lagunare che anima le domeniche di febbraio con grandi sfilate di carri allegorici in cartapesta, maschere a tema, corpi bandistici e il corteo trionfale di Re Carnevale. Stand gastronomici e chioschi con i dolci tradizionali della festa (frittelle di riso maremmane, cenci fritti caldi e castagnole), musica dal vivo in piazza e festa notturna finale con la proclamazione del 'Carrissimo'.",
        "Giorni Effettivi": "Tutte le domeniche di febbraio e sfilata notturna finale",
        "Valutazione": "⭐⭐⭐⭐⭐ (4.8)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🎭 Grande Sfilata dei Carri Allegorici</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Tutte le domeniche di Febbraio dalle ore 14:30: Apertura del circuito cittadino nel cuore di Orbetello.</li><li>Ore 15:00: Grandiosa parata dei giganteschi carri allegorici in cartapesta lungo Corso Italia, scortati da bande musicali, gruppi mascherati in coreografie spettacolari, Re Carnevale e la corte delle Reginette.</li><li>Lancio continuo di coriandoli, stelle filanti e gadget per la gioia di grandi e piccini.</li><li>Domenica 28 Febbraio (Gran Finale): Spettacolare sfilata notturna illuminata con fuochi d\'artificio e proclamazione del carro vincitore del trofeo "Carrissimo 2027".</li></ul><p class="mb-2 text-maremma-700"><strong>🍩 I Dolci Tipici di Carnevale</strong></p><ul class="list-disc pl-5 space-y-1"><li>Chioschi gastronomici aperti per tutto il percorso con le dolci tradizioni toscane: cenci fritti spolverati di zucchero a velo, calde frittelle di riso di San Giuseppe e bomboloni ripieni alla crema.</li></ul>'
    },
    {
        "Data Inizio": "08/05/2027",
        "Data Fine": "09/05/2027",
        "Nome Evento": "Sui Sentieri del Prugnolo (Festa al Prugnolo)",
        "Comune / Frazione": "Montieri",
        "Luogo Esatto": "Centro storico e boschi di Montieri",
        "Descrizione dell'Evento": "Celebrazione primaverile dedicata al ricercatissimo e profumato fungo prugnolo (Tricholoma georgii) delle Colline Metallifere. Stand gastronomici con primi piatti e specialità a base di prugnolo fresco, escursioni micologiche guidate nei boschi circostanti, mercatino biologico e dell'artigianato, show cooking e intrattenimento per le vie del borgo.",
        "Giorni Effettivi": "Sabato e Domenica",
        "Valutazione": "⭐⭐⭐⭐½ (4.5)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🍄 Gastronomia & Fungo Prugnolo a Km 0</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Ristorante della Pro Loco nel centro di Montieri dedicato al pregiato fungo prugnolo (<em>Tricholoma georgii</em>) colto nei boschi metalliferi: tagliolini e tortelli al prugnolo, arrosti profumati, crostoni e piatti della tradizione contadina.</li><li>Apertura stand: Sabato a cena dalle 19:30; Domenica sia a pranzo (dalle 12:30) che a cena (dalle 19:30).</li></ul><p class="mb-2 text-maremma-700"><strong>🌿 Escursioni, Mostre & Mercatini</strong></p><ul class="list-disc pl-5 space-y-1"><li><strong>Sabato:</strong> Ore 15:30 apertura della mostra micologica ed escursione guidata nei boschi con esperti per il riconoscimento delle erbe e dei funghi primaverili; musica dal vivo in piazza alla sera.</li><li><strong>Domenica:</strong> Dalle ore 09:30 mostra mercato di prodotti tipici locali e artigianato; ore 10:00 trekking guidato "Sui sentieri dei minatori"; nel pomeriggio show cooking in piazza e animazione per famiglie.</li></ul>'
    },
    {
        "Data Inizio": "28/05/2027",
        "Data Fine": "30/05/2027",
        "Nome Evento": "Sagra della Lumaca Riganella",
        "Comune / Frazione": "Manciano (Fraz. Poggio Murella)",
        "Luogo Esatto": "Piazza del Popolo e centro del borgo, Poggio Murella",
        "Descrizione dell'Evento": "Tradizionale festa organizzata dalla storica Filarmonica 'P. Mascagni'. La protagonista è la 'lumaca riganella', cucinata secondo un'antica e laboriosa ricetta locale a base di erbe aromatiche e spezie, affiancata dai celebri 'lunghini' (pasta fresca rustica tirata a mano), acquacotta maremmana, carni alla brace, ballo liscio e orchestre dal vivo.",
        "Giorni Effettivi": "Solo fine settimana (Venerdì e Sabato cena, Domenica pranzo e cena)",
        "Valutazione": "⭐⭐⭐⭐½ (4.6)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🐌 Stand Gastronomici & Ricetta della Tradizione</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Festa organizzata dalla centenaria Filarmonica "P. Mascagni" a Poggio Murella.</li><li>Piatto forte la celeberrima "lumaca riganella", preparata con un\'antica e minuziosa ricetta a lenta cottura arricchita da spezie ed erbe spontanee maremmane.</li><li>Ricco menù contadino: i tradizionali "lunghini" (pasta fresca acqua e farina tirata a mano), acquacotta maremmana, carne alla brace, salsicce toscane e bruschette al pomodoro.</li><li>Stand aperti venerdì e sabato a cena (dalle 19:30), domenica anche a pranzo (dalle 12:30).</li></ul><p class="mb-2 text-maremma-700"><strong>🎺 Musica dal Vivo & Serate Danzanti</strong></p><ul class="list-disc pl-5 space-y-1"><li>Ogni sera grande concerto e ballo liscio all\'aperto in Piazza del Popolo con la Filarmonica "P. Mascagni" e rinomate orchestre toscane.</li></ul>'
    },
    {
        "Data Inizio": "02/07/2027",
        "Data Fine": "01/08/2027",
        "Nome Evento": "Festa dello Sport e del Cinghiale alla Cacciatora",
        "Comune / Frazione": "Grosseto (Fraz. Rispescia)",
        "Luogo Esatto": "Impianti Sportivi, Rispescia (Grosseto)",
        "Descrizione dell'Evento": "Storica sagra estiva alle porte del Parco Naturale della Maremma. Protagonista assoluto il cinghiale cucinato alla cacciatora secondo la ricetta tradizionale dei cacciatori maremmani, insieme a tortelli fatti a mano, panzanella fresca, acquacotta e brace mista, con serate danzanti, orchestre e animazione per famiglie.",
        "Giorni Effettivi": "Tutti i weekend di luglio (Venerdì, Sabato e Domenica sera)",
        "Valutazione": "⭐⭐⭐⭐½ (4.5)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🐗 Ristorante Gastronomico Maremmano</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Stand gastronomici coperti attivi tutti i fine settimana di Luglio (Venerdì, Sabato e Domenica) dalle ore 19:30 presso gli Impianti Sportivi di Rispescia.</li><li>Regina del menù la cacciagione locale: cinghiale alla cacciatora a cottura lenta in umido, tortelli maremmani fatti a mano al ragù di cinghiale, acquacotta della tradizione buttera, tagliatelle caserecce, panzanella estiva e grigliate di maiale e vitello.</li><li>Ampia selezione di vini Morellino di Scansano e Maremma Toscana DOC.</li></ul><p class="mb-2 text-maremma-700"><strong>⚽ Sport, Ballo & Divertimento</strong></p><ul class="list-disc pl-5 space-y-1"><li>Dalle ore 21:00 pista da ballo all\'aperto con serate danzanti, le migliori orchestre di liscio e balli di gruppo.</li><li>Tornei serali di calcetto, giochi per bambini e spazi ricreativi per tutta la famiglia.</li></ul>'
    },
    {
        "Data Inizio": "23/07/2027",
        "Data Fine": "01/08/2027",
        "Nome Evento": "Sagra del Moscardino e del Polpetto",
        "Comune / Frazione": "Orbetello (Fraz. Talamone)",
        "Luogo Esatto": "Sporting Club Talamone, Via Cala di Forno, Talamone",
        "Descrizione dell'Evento": "Tradizionale appuntamento con la cucina marinara nella splendida baia sotto la rocca di Talamone. Specialità assoluta il prelibato 'polpetto alla talamonese' in umido, frittura croccante di moscardini e paranza, insalate di mare fresche e primi piatti ai profumi del Tirreno, con musica dal vivo e serate sotto le stelle.",
        "Giorni Effettivi": "Tutte le sere dalle 19:30",
        "Valutazione": "⭐⭐⭐⭐½ (4.6)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🐙 Sapori di Mare a Talamone</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Rassegna culinaria marinara nella splendida cornice dello Sporting Club di Talamone (Via Cala di Forno), aperta tutte le sere dalle ore 19:30.</li><li>Specialità imperdibile: il tradizionale "polpetto alla talamonese" cotto in umido con pomodoro e aromi mediterranei, accompagnato da croccante frittura espressa di moscardini e paranza tirrenica.</li><li>Menù marinaro: spaghetti ai frutti di mare, insalata tiepida di mare, pesce alla griglia e bruschette marinare, con opzioni di terra per accontentare tutti i palati.</li></ul><p class="mb-2 text-maremma-700"><strong>🎶 Serate sotto la Rocca</strong></p><ul class="list-disc pl-5 space-y-1"><li>Dalle 21:30 musica dal vivo, pianobar, cocktail bar fronte mare e intrattenimento sotto la brezza della rocca medievale aldobrandesca.</li></ul>'
    },
    {
        "Data Inizio": "29/07/2027",
        "Data Fine": "08/08/2027",
        "Nome Evento": "Sagra del Baccalà",
        "Comune / Frazione": "Magliano in Toscana (Fraz. Sant'Andrea)",
        "Luogo Esatto": "Campo Sportivo di Sant'Andrea al Civilesco, Magliano in Toscana",
        "Descrizione dell'Evento": "Una delle sagre più attese e longeve dell'estate maremmana (giunta a oltre 35 edizioni), curata dall'A.S.D. Magliano Sant'Andrea. Il baccalà è servito in innumerevoli varianti d'eccellenza: fritto dorato, in umido con ceci, alla brace, in insalata e come ripieno o condimento di tortelli fatti a mano, accompagnato dai grandi vini delle colline maglianesi e musica dal vivo tutte le sere.",
        "Giorni Effettivi": "Tutte le sere a cena",
        "Valutazione": "⭐⭐⭐⭐⭐ (4.8)",
        "Programma Dettagliato": '<p class="mb-2 text-maremma-700"><strong>🐟 Oltre 35 Anni di Tradizione del Baccalà</strong></p><ul class="list-disc pl-5 mb-4 space-y-1"><li>Storica sagra curata con passione dall\'A.S.D. Magliano Sant\'Andrea al campo sportivo di Sant\'Andrea al Civilesco.</li><li>Stand gastronomici aperti tutte le sere dalle 19:30 con un menù ricchissimo interamente dedicato al baccalà:<ul class="list-disc pl-5 mt-1 space-y-0.5"><li><strong>Primi:</strong> Tortelli maremmani al sugo di baccalà, penne e tagliatelle al baccalà, zuppa tradizionale.</li><li><strong>Secondi:</strong> Gran fritto dorato di baccalà, baccalà alla livornese con pomodoro e cipolle, baccalà alla brace e insalata fresca di baccalà e ceci.</li><li>Piatti alternativi di terra: carni alla griglia, tortelli al ragù classico toscano e contorni freschi.</li></ul></li><li>Vini locali delle colline di Magliano in Toscana.</li></ul><p class="mb-2 text-maremma-700"><strong>💃 Musica & Spettacoli</strong></p><ul class="list-disc pl-5 space-y-1"><li>Ogni sera dalle ore 21:15 spettacoli musicali gratuiti con grandi orchestre da ballo liscio, cover band e momenti di cabaret.</li></ul>'
    }
]

# Read existing file
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Check for existing events by exact name or location
existing_names = [r[2].strip().lower() for r in rows if len(r) >= 3]

added_count = 0
for ev in new_events:
    name_norm = ev["Nome Evento"].strip().lower()
    if name_norm in existing_names:
        print(f"Evento già presente, salto: {ev['Nome Evento']}")
        continue
    
    # Construct row in header order
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
    added_count += 1
    print(f"Aggiunto: {ev['Nome Evento']}")

# Helper for date sorting
def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), '%d/%m/%Y')
    except Exception:
        return datetime.max

# Sort chronologically by start date, then end date
rows.sort(key=lambda r: (parse_date(r[0]), parse_date(r[1]) if len(r) > 1 else datetime.max))

# Write back sorted CSV
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"\nOperazione completata: inseriti {added_count} nuovi eventi.")
print(f"Totale eventi in {file_path}: {len(rows)}.")
