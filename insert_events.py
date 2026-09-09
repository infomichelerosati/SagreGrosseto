import csv
from datetime import datetime

new_events = [
    ["03/09/2026", "13/09/2026", "Festa di Fine Estate", "Sorano (Fraz. San Giovanni delle Contee)", "Centro del borgo e area festeggiamenti, San Giovanni delle Contee", "Tradizionale festa paesana e religiosa in onore di Maria SS. Addolorata con stand gastronomici e tipica 'fraschetta' aperta tutte le sere, piatti tipici dell'alta Maremma, musica dal vivo, ballo liscio e la divertente 'Corrida' paesana.", "3-6 e 11-13 Settembre (tutte le sere da giovedì a domenica)", "⭐⭐⭐⭐ (4.3)", ""],
    ["04/09/2026", "13/09/2026", "Settembre Roccastradino (54ª Edizione)", "Roccastrada", "Parco del Chiusone e vie del centro storico, Roccastrada", "Storica rassegna decennale con grande ristorante gastronomico a tema culinario ogni sera (serate dedicate a baccalà, strozzapreti all'aglione, peposo, maialino al forno, lumache e cacciagione), eventi sportivi, musica live, sfilata e l'atteso Palio Umoristico dei Ciuchi con fuochi d'artificio finali.", "Tutte le sere (e a pranzo nei fine settimana)", "⭐⭐⭐⭐⭐ (4.8)", ""],
    ["07/09/2026", "13/09/2026", "Palio dei Ciuchi e Tradizioni di Campagnatico (69ª Edizione)", "Campagnatico", "Centro storico, Via Roma e Rocca Aldobrandesca, Campagnatico", "Settimana di festa della comunità locale tra corteo medievale con oltre 100 figuranti, banchetto signorile 'Alla corte di Umberto', serate gastronomiche con piatti tipici e l'avvincente 69ª corsa del Palio dei Ciuchi tra i quattro rioni storici (Castello, Centro, Pieve, Santa Maria).", "Da lunedì a domenica (Palio la domenica pomeriggio)", "⭐⭐⭐⭐⭐ (4.8)", ""],
    ["11/09/2026", "13/09/2026", "La Stortellata (Festa del Tortello di Selvena)", "Castell'Azzara (Fraz. Selvena)", "Parco Verde, Selvena", "Amata sagra amiatina dedicata al tradizionale tortello di patate selvignano, preparato a mano con la rara patata biancona del Faggeto. Stand gastronomico ruspante con primi piatti fatti in casa, carni alla brace e musica all'aperto.", "Venerdì e Sabato a cena, Domenica a pranzo", "⭐⭐⭐⭐½ (4.5)", ""],
    ["19/09/2026", "04/10/2026", "Sagra della Polenta a Bivio di Ravi", "Gavorrano (Fraz. Bivio di Ravi)", "Struttura coperta polivalente, Bivio di Ravi, Gavorrano", "Celebre e atteso appuntamento autunnale che celebra la polenta cotta nel paiolo e condita con ricchi sughi tradizionali di cinghiale, capriolo, funghi porcini e salsiccia. Stand coperti, orchestre e serate danzanti.", "Solo fine settimana (19-20, 26-27 sett. e 3-4 ott.; Sabato cena, Domenica pranzo e cena)", "⭐⭐⭐⭐½ (4.6)", ""],
    ["24/09/2026", "27/09/2026", "Festa dell'Uva e delle Cantine al Giglio", "Isola del Giglio (Fraz. Giglio Castello)", "Vicoli, piazze e cantine storiche di Giglio Castello", "Festa clou dell'isola che celebra la fine della vendemmia. Apertura serale delle cantine scavate nella roccia con degustazioni del celebre vino Ansonaco, cavatelli gigliesi, coniglio alla cacciatora, pesce locale e panficato gigliese, allietati da canti tradizionali e musica itinerante.", "Da giovedì a sabato a cena (dalle 19:30), domenica a pranzo (dalle 12:30)", "⭐⭐⭐⭐⭐ (4.9)", ""],
    ["27/09/2026", "27/09/2026", "Festa Contadina di Tirli in Rosa", "Castiglione della Pescaia (Fraz. Tirli)", "Centro storico e piazze del borgo, Tirli", "Giornata dedicata alla memoria contadina e alle specialità culinarie dei boschi e delle colline castiglionesi. Grande pranzo contadino conviviale all'aperto, esposizione e vendita di prodotti tipici locali e artigianato.", "Domenica dalle ore 10:30 (pranzo contadino)", "⭐⭐⭐⭐ (4.3)", ""],
    ["03/10/2026", "04/10/2026", "Festa della Castagna Ciola e Raduno d'Autunno", "Castel del Piano", "Centro storico e Piazza Madonna, Castel del Piano", "Primo evento amiatino dedicato alla 'Castagna Ciola' di Castel del Piano. Degustazione di caldarroste, necci, castagnaccio e birre artigianali di castagna, accompagnati da musica dal vivo e dal raduno motociclistico d'autunno.", "Sabato e Domenica", "⭐⭐⭐⭐½ (4.5)", ""],
    ["24/10/2026", "25/10/2026", "Festa del Marrone Santafiorese", "Santa Fiora", "Centro storico e Parco della Peschiera, Santa Fiora", "Tradizionale appuntamento autunnale inserito nel circuito AmiatAutunno dedicato alla castagna IGP del Monte Amiata. Stand gastronomici con piatti a base di farina dolce e 'castrate' (castagne arrostite sul fuoco), mercatini artigianali ed escursioni guidate tra i castagneti.", "Sabato e Domenica", "⭐⭐⭐⭐½ (4.6)", ""],
    ["24/11/2026", "24/11/2026", "Focarazza di Santa Caterina (Rito del Fuoco e Palio dello Stollo)", "Roccalbegna (Fraz. Santa Caterina)", "Poggio alle Forche e centro del borgo, Santa Caterina", "Antichissimo e spettacolare rito del fuoco alla vigilia della patrona: accensione della monumentale catasta di fascine con al centro lo 'stollo' di cerro, seguita dall'acceso Palio dello Stollo tra le contrade per aggiudicarsi il tronco incandescente. Stand gastronomici con salsicce alla brace, fegatelli, dolci locali e vino caldo.", "Pomeriggio e sera del 24 Novembre", "⭐⭐⭐⭐⭐ (4.8)", ""],
    ["28/11/2026", "29/11/2026", "ÒLEA - Festa dell'Olio Novo di Giuncarico", "Gavorrano (Fraz. Giuncarico)", "Borgo medievale e vie del centro, Giuncarico", "Rassegna autunnale che valorizza l'oro verde della Maremma con degustazioni guidate di olio extravergine d'oliva appena franto, stand enogastronomici a km zero (bruschette calde, zuppe toscane), mercatini dell'olio, trekking tra gli oliveti e concerti nei vicoli.", "Sabato e Domenica", "⭐⭐⭐⭐½ (4.6)", ""],
    ["28/11/2026", "29/11/2026", "Olionovo a Pereta", "Magliano in Toscana (Fraz. Pereta)", "Centro storico e vicoli medievali, Pereta", "Manifestazione per celebrare l'olio nuovo appena spremuto dei frantoi maglianesi, con concorso per il miglior olio, stand con bruschette all'olio novo, caldarroste, porchetta, salsicce alla brace, vin brulé, spettacoli di strada e passeggiate tra gli olivi.", "Sabato e Domenica", "⭐⭐⭐⭐½ (4.5)", ""],
    ["30/12/2026", "30/12/2026", "Fiaccolata di Santa Fiora (Notte delle Fiaccole e delle Frasche)", "Santa Fiora", "Piazza Garibaldi e centro storico medievale, Santa Fiora", "Magica e millenaria festa del fuoco che accende la notte di fine anno con le monumentali 'carboniere' (grandi piramidi di legna accese dai minatori), processione con le torce e apertura delle 'frasche' (caratteristici punti ristoro) con zuppe calde amiatine, grigliate di carne, dolci della tradizione e vin brulé.", "Sera del 30 Dicembre (dalle ore 18:00 a notte inoltrata)", "⭐⭐⭐⭐⭐ (4.9)", ""],
    ["31/12/2026", "31/12/2026", "Focarazza di San Silvestro", "Manciano (Fraz. Saturnia)", "Piazza Vittorio Veneto, Saturnia", "Tradizionale e suggestiva festa popolare della notte di Capodanno con accensione del grande falò conico purificatore al centro della piazza alle ore 22:00. Stand con bruschette maremmane, salsicce alla brace, dolci tipici e vin brulé, seguiti da musica dal vivo, DJ set e brindisi di mezzanotte sotto le stelle.", "Notte di San Silvestro (31 Dicembre)", "⭐⭐⭐⭐½ (4.6)", ""]
]

def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), '%d/%m/%Y')
    except:
        return datetime.max

file_path = 'c:\\Users\\miche\\Desktop\\SAGRE GROSSETO\\sagre.csv'
header = []
events = []

with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if len(row) >= 3: # Must have at least name and dates
            # Ensure the row has exactly the length of the header
            while len(row) < len(header):
                row.append('')
            events.append(row)

# Append new events
for event in new_events:
    # Match header length
    while len(event) < len(header):
        event.append('')
    events.append(event)

# Sort events chronologically by start date
events.sort(key=lambda x: parse_date(x[0]))

# Write back
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(events)

print("Insertion and sorting complete.")
