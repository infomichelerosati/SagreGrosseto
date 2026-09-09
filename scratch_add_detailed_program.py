import csv
import sys

file_path = 'sagre.csv'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print("sagre.csv not found!")
    sys.exit(1)

header = data[0]

# Add 'Programma Dettagliato' to header if missing
if "Programma Dettagliato" not in header:
    header.append("Programma Dettagliato")
    for row in data[1:]:
        row.append("")
    
prog_index = header.index("Programma Dettagliato")
name_index = header.index("Nome Evento")

# The HTML content for Santa Lucia
santa_lucia_html = """<p class="mb-2 text-maremma-700"><strong>🍽️ Stand Gastronomici</strong></p>
<ul class="list-disc pl-5 mb-4 space-y-1">
  <li>Tutti i giorni dalle ore 18:00 apertura del bar e della fiera di beneficenza.</li>
  <li>Dalle ore 19:00 apertura del ristorante "Simone Pellegrini" con specialità tipiche e carne alla griglia.</li>
  <li>Ogni sera alle 21:30 il classico appuntamento con la Tombola, accompagnata da concerti gratuiti dal vivo!</li>
</ul>
<p class="mb-2 text-maremma-700"><strong>🎵 Il Programma Musicale (Inizio live ore 21:15)</strong></p>
<ul class="list-disc pl-5 space-y-1">
  <li><strong>Giovedì 10 Settembre:</strong> Processione in onore di Santa Lucia seguita dal concerto della Filarmonica di Grosseto.</li>
  <li><strong>Venerdì 11 Settembre:</strong> Pianeta Zero (Renato Zero Tribute Band).</li>
  <li><strong>Sabato 12 Settembre:</strong> Mama Lover (Dance Party anni '80-'90-2000).</li>
  <li><strong>Domenica 13 Settembre:</strong> False Partenze (Big Band jazz/swing) - Al mattino (ore 11) S. Messa col Vescovo.</li>
  <li><strong>Lunedì 14 Settembre:</strong> Lo storico Coro dei Minatori di Santa Fiora.</li>
  <li><strong>Martedì 15 Settembre:</strong> Rino Gaetano Band.</li>
  <li><strong>Mercoledì 16 Settembre:</strong> Beatbox (The Beatles Tribute Band).</li>
  <li><strong>Giovedì 17 Settembre:</strong> Grande concerto di Eugenio Finardi (Tutto Finardi Live 2026).</li>
  <li><strong>Venerdì 18 Settembre:</strong> Rubbish (Oasis Tribute Band).</li>
  <li><strong>Sabato 19 Settembre:</strong> Rubami la Notte (Pinguini Tattici Nucleari Tribute Band).</li>
  <li><strong>Domenica 20 Settembre:</strong> Grande chiusura con il 39° Festival Canoro Baby (pomeriggio) e il live di Francesco Di Napoli alla sera.</li>
</ul>"""

# Apply to Santa Lucia
found = False
for row in data[1:]:
    if "Santa Lucia" in row[name_index]:
        # Ensure row has enough columns
        while len(row) <= prog_index:
            row.append("")
        row[prog_index] = santa_lucia_html.replace('\n', '') # Removing newlines for cleaner CSV string
        found = True

if not found:
    print("Festa di Santa Lucia non trovata nel CSV!")
    sys.exit(1)

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Programma dettagliato aggiunto con successo a sagre.csv!")
