new_events = [
    '17/07/2026,19/07/2026,Sagra del Lunghino,Manciano (Fraz. Poggio Murella),"Piazza centrale, Poggio Murella","14ª edizione dedicata al \'lunghino\', la tipica pasta fresca locale fatta a mano, servita con sughi tradizionali.",Solo fine settimana,⭐⭐⭐⭐ (4.4)\n',
    '17/07/2026,19/07/2026,Sbraciata del Buttero,Scansano (Fraz. Pomonte),"Area Feste, Pomonte","Rassegna dedicata all\'autentica carne alla brace maremmana, tra tradizioni equestri e i celebri butteri.",Solo fine settimana,⭐⭐⭐⭐ (4.5)\n'
]
with open('c:\\\\Users\\\\miche\\\\Desktop\\\\SAGRE GROSSETO\\\\sagre.csv', 'a', encoding='utf-8') as f:
    f.writelines(new_events)
