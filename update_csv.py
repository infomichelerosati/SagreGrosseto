# -*- coding: utf-8 -*-
import csv

input_file = "sagre.csv"
output_file = "sagre_updated.csv"

giorni_effettivi_map = {
    "Sagra degli Strozzapreti e dei prodotti tipici maremmani": "Aperta solo nel fine settimana (Ven-Dom)",
    "Sagra del Dolce Casalingo": "Solo weekend",
    "Festa dello Sport e del Tortello (Sagra del Tortello al Cristo)": "Tutti i weekend (Sab e Dom) e Ferragosto",
    "Sarde e Calamari in Festa": "Solo i fine settimana",
    "Sagra del Baccalà": "Dal venerdì alla domenica",
    "Sagra di Campagnatico": "Aperta tutti i giorni",
    "Sagra a Buriano": "Solo dal giovedì alla domenica",
    "Festa del Cinghiale Maremmano": "Solo weekend e prefestivi",
    "Sagra del tortello maremmano": "Tutti i giorni",
    "Sagra della Ficamaschia Dorata": "Tutti i giorni",
    "Sagra d''Estate": "Weekend di agosto",
    "Sagra del Tortello e Maccherone maremmano": "Solo fine settimana",
    "Sagra della Granocchia": "Solo 29-30 agosto e 5-6 settembre",
    "Castagna in Festa": "Solo nei fine settimana (Ven-Dom)"
}

with open(input_file, mode="r", encoding="utf-8") as infile, open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)
    header.insert(6, "Giorni Effettivi")
    writer.writerow(header)
    
    for row in reader:
        if len(row) < 3:
            continue
        nome_evento = row[2]
        try:
            d_inizio = int(row[0].split("/")[0])
            d_fine = int(row[1].split("/")[0])
            m_inizio = int(row[0].split("/")[1])
            m_fine = int(row[1].split("/")[1])
            durata = (d_fine - d_inizio) + (m_fine - m_inizio)*30
        except:
            durata = 0
            
        giorni = giorni_effettivi_map.get(nome_evento, "")
        if not giorni and durata > 5:
            giorni = "Solo fine settimana"
            
        row.insert(6, giorni)
        writer.writerow(row)
