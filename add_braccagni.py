new_events = [
    '15/07/2026,15/07/2026,Country Roads con Black Carpet Trio,Grosseto (Fraz. Braccagni),"Struttura Polivalente, Braccagni","Serata speciale di mezza estate dedicata alla musica country, folk e rock americano. Presente punto ristoro con ottimi panini e birra.",Singola serata,⭐⭐⭐⭐ (4.4)\n',
    '17/07/2026,17/07/2026,Loco Magic (Illusionismo e Magia),Grosseto (Fraz. Braccagni),"Struttura Polivalente, Braccagni","Spettacolo di illusionismo e magia per tutta la famiglia organizzato dalla Pro Loco di Braccagni e Montepescali.",Singola serata,⭐⭐⭐⭐ (4.2)\n'
]
with open('c:\\\\Users\\\\miche\\\\Desktop\\\\SAGRE GROSSETO\\\\sagre.csv', 'a', encoding='utf-8') as f:
    f.writelines(new_events)
