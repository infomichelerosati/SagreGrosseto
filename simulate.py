import csv
from datetime import datetime

today = datetime(2026, 7, 3, 11, 57, 40)

def parse_date(date_str):
    try:
        parts = date_str.strip().split('/')
        return datetime(int(parts[2]), int(parts[1]), int(parts[0]))
    except:
        return None

with open('sagre.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        start = parse_date(row[0])
        end = parse_date(row[1])
        if start and end:
            status = ""
            if today >= start and today <= end:
                status = "In Corso"
            elif today < start:
                status = "In Arrivo"
            else:
                status = "Conclusa"
            
            if status == "In Corso":
                print(f"In Corso: {row[2]} ({row[0]} - {row[1]})")
