import csv
import os
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

file_path = 'sagre.csv'
out_dir = 'eventi'
site_url = 'https://sagre.spiritoindomito.it'

import glob

if not os.path.exists(out_dir):
    os.makedirs(out_dir)
else:
    # Pulisce i vecchi file html per gestire le eliminazioni dal CSV
    for f in glob.glob(os.path.join(out_dir, "*.html")):
        os.remove(f)

# Leggi CSV
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    events = list(reader)

sitemap_urls = []
sitemap_urls.append(f"""  <url>
    <loc>{site_url}/</loc>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

html_template = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Sagre Grosseto</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="article">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        h1, h2, h3 {{ font-family: 'Playfair Display', serif; }}
    </style>
    <script type="application/ld+json">
    {json_ld}
    </script>
</head>
<body class="bg-[#fdf8f5] text-slate-800 min-h-screen flex flex-col">
    <header class="bg-gradient-to-r from-[#283618] to-[#4c1a06] text-white py-6 shadow-lg">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <a href="../index.html" class="inline-block text-[#f5d9ca] hover:text-white mb-2 text-sm uppercase tracking-wider font-semibold transition-colors">&larr; Torna al Calendario Completo</a>
            <h1 class="text-3xl md:text-4xl font-bold mt-2">{name}</h1>
            <p class="mt-2 text-[#fbeee6] text-lg">{location}</p>
        </div>
    </header>
    <main class="flex-grow max-w-4xl mx-auto px-4 py-12 w-full">
        <div class="bg-white rounded-3xl shadow-xl border border-slate-100 p-8 md:p-12">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-100">
                    <p class="text-xs text-slate-400 uppercase font-bold tracking-wider mb-1">Date dell'evento</p>
                    <p class="text-xl font-bold text-slate-700">{start_date} - {end_date}</p>
                    <p class="text-sm text-slate-500 mt-2">Giorni effettivi: {giorni}</p>
                </div>
                <div class="bg-slate-50 p-6 rounded-2xl border border-slate-100">
                    <p class="text-xs text-slate-400 uppercase font-bold tracking-wider mb-1">Luogo Esatto</p>
                    <p class="text-lg font-bold text-slate-700">{exact_location}</p>
                    <p class="text-sm text-slate-500 mt-2">Valutazione: {rating}</p>
                </div>
            </div>
            
            <h2 class="text-2xl font-bold text-slate-800 mb-4 border-b border-slate-100 pb-2">Dettagli dell'Evento</h2>
            <div class="prose max-w-none text-slate-700 leading-relaxed text-lg">
                {rich_program}
            </div>

            <div class="mt-12 text-center">
                <a href="../index.html" class="inline-block bg-[#d96b27] hover:bg-[#b24f1c] text-white font-bold py-3 px-8 rounded-xl transition-all shadow-md hover:shadow-lg">
                    Vedi tutte le sagre in Maremma
                </a>
            </div>
        </div>
    </main>
    <footer class="bg-slate-900 text-slate-400 py-8 text-center text-sm">
        <p>&copy; 2026 Sagre Grosseto. Tutti i diritti riservati.</p>
    </footer>
</body>
</html>
"""

for ev in events:
    name = ev.get("Nome Evento", "")
    comune = ev.get("Comune / Frazione", "")
    start_date = ev.get("Data Inizio", "")
    end_date = ev.get("Data Fine", "")
    desc = ev.get("Descrizione dell'Evento", "")
    exact_loc = ev.get("Luogo Esatto", "")
    giorni = ev.get("Giorni Effettivi", "")
    rating = ev.get("Valutazione", "")
    prog = ev.get("Programma Dettagliato", "")

    # Cleanup dates for JSON-LD (from DD/MM/YYYY to YYYY-MM-DD)
    iso_start = ""
    iso_end = ""
    try:
        if start_date: iso_start = "-".join(start_date.split("/")[::-1])
        if end_date: iso_end = "-".join(end_date.split("/")[::-1])
    except:
        pass

    slug = slugify(f"{name} {comune}")
    if not slug: continue
    
    file_name = f"{slug}.html"
    page_url = f"{site_url}/eventi/{file_name}"
    
    # Metadata
    page_title = f"{name} a {comune} | Sagre Grosseto {start_date[-4:] if start_date else ''}"
    clean_desc = desc.replace('"', '&quot;')
    
    rich_program = prog if prog else f"<p>{desc}</p>"

    json_ld = f"""{{
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "{name}",
      "description": "{clean_desc}",
      "startDate": "{iso_start}",
      "endDate": "{iso_end}",
      "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
      "eventStatus": "https://schema.org/EventScheduled",
      "location": {{
        "@type": "Place",
        "name": "{exact_loc}",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{comune}",
          "addressRegion": "Toscana",
          "addressCountry": "IT"
        }}
      }},
      "image": [
        "https://sagre.spiritoindomito.it/images/default-sagra.jpg"
      ],
      "organizer": {{
        "@type": "Organization",
        "name": "Comitato Festeggiamenti {comune}",
        "url": "{page_url}"
      }},
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "EUR",
        "availability": "https://schema.org/InStock",
        "url": "{page_url}",
        "validFrom": "{iso_start}"
      }},
      "performer": {{
        "@type": "PerformingGroup",
        "name": "Artisti e Band Locali"
      }}
    }}"""

    html_content = html_template.format(
        title=page_title,
        description=clean_desc,
        url=page_url,
        name=name,
        location=comune,
        start_date=start_date,
        end_date=end_date,
        exact_location=exact_loc,
        giorni=giorni,
        rating=rating,
        rich_program=rich_program,
        json_ld=json_ld
    )

    with open(os.path.join(out_dir, file_name), 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Add to sitemap
    sitemap_urls.append(f"""  <url>
    <loc>{page_url}</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

# Generate new sitemap.xml
sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Generated {len(events)} SEO static pages and updated sitemap.xml.")
