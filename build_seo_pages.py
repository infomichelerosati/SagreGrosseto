# -*- coding: utf-8 -*-
import csv
import os
import re
import glob
from datetime import datetime

def slugify(text):
    text = text.lower()
    # Normalize accents
    text = re.sub(r'[àáâãäå]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

file_path = 'sagre.csv'
out_dir = 'eventi'
site_url = 'https://sagre.spiritoindomito.it'

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

# Pre-compute slugs for all events
for ev in events:
    name = ev.get("Nome Evento", "")
    comune = ev.get("Comune / Frazione", "")
    ev['slug'] = slugify(f"{name} {comune}")

html_template = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="icon" href="/icons/icon-192x192.png" type="image/png">
    <meta name="description" content="{description}">
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="article">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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
            <nav class="text-xs text-[#f5d9ca] mb-2 flex items-center justify-center gap-1.5" aria-label="Breadcrumb">
                <a href="https://sagre.spiritoindomito.it/" class="hover:underline">Home</a>
                <span>&gt;</span>
                <a href="https://sagre.spiritoindomito.it/" class="hover:underline">Sagre Grosseto</a>
                <span>&gt;</span>
                <span class="text-white font-medium">{name}</span>
            </nav>
            <h1 class="text-3xl md:text-4xl font-bold mt-2">{name}</h1>
            <p class="mt-2 text-[#fbeee6] text-lg">{location}</p>
        </div>
    </header>
    <main class="flex-grow max-w-4xl mx-auto px-4 py-8 md:py-12 w-full">
        <div class="bg-white rounded-3xl shadow-xl border border-slate-100 p-6 md:p-12">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-8 mb-8">
                <div class="bg-slate-50 p-5 md:p-6 rounded-2xl border border-slate-100">
                    <p class="text-xs text-slate-400 uppercase font-bold tracking-wider mb-1">Date dell'evento</p>
                    <p class="text-lg md:text-xl font-bold text-slate-700">{start_date} - {end_date}</p>
                    <p class="text-sm text-slate-500 mt-2">Giorni effettivi: {giorni}</p>
                </div>
                <div class="bg-slate-50 p-5 md:p-6 rounded-2xl border border-slate-100">
                    <p class="text-xs text-slate-400 uppercase font-bold tracking-wider mb-1">Luogo Esatto</p>
                    <p class="text-base md:text-lg font-bold text-slate-700">{exact_location}</p>
                    <p class="text-sm text-slate-500 mt-2">Valutazione: {rating}</p>
                </div>
            </div>
            
            <h2 class="text-xl md:text-2xl font-bold text-slate-800 mb-4 border-b border-slate-100 pb-2">Dettagli dell'Evento e Programma</h2>
            <div class="prose max-w-none text-slate-700 leading-relaxed text-base md:text-lg">
                {rich_program}
            </div>

            <!-- Box Altre Sagre Correlate (Mesh Linking SEO) -->
            {related_section}

            <div class="mt-10 text-center">
                <a href="https://sagre.spiritoindomito.it/" class="inline-block bg-[#d96b27] hover:bg-[#b24f1c] text-white font-bold py-3 px-8 rounded-xl transition-all shadow-md hover:shadow-lg">
                    ← Torna al calendario completo di tutte le sagre
                </a>
            </div>
        </div>
    </main>
    <footer class="bg-slate-900 text-slate-400 py-8 text-center text-sm space-y-2">
        <p>&copy; 2026 Sagre Grosseto. Portale gratuito per la valorizzazione del territorio e delle sagre maremmane.</p>
        <p class="text-xs text-slate-500">🔒 Privacy 100%: Nessun tracciamento, nessun dato personale raccolto, nessun cookie di profilazione.</p>
    </footer>
</body>
</html>
"""

for idx, ev in enumerate(events):
    name = ev.get("Nome Evento", "")
    comune = ev.get("Comune / Frazione", "")
    start_date = ev.get("Data Inizio", "")
    end_date = ev.get("Data Fine", "")
    desc = ev.get("Descrizione dell'Evento", "")
    exact_loc = ev.get("Luogo Esatto", "")
    giorni = ev.get("Giorni Effettivi", "")
    rating = ev.get("Valutazione", "")
    prog = ev.get("Programma Dettagliato", "")
    slug = ev.get("slug", "")

    if not slug:
        continue

    # Cleanup dates for JSON-LD (from DD/MM/YYYY to YYYY-MM-DD)
    iso_start = ""
    iso_end = ""
    try:
        if start_date: iso_start = "-".join(start_date.split("/")[::-1])
        if end_date: iso_end = "-".join(end_date.split("/")[::-1])
    except:
        pass

    file_name = f"{slug}.html"
    page_url = f"{site_url}/eventi/{file_name}"
    
    # Metadata
    year_str = start_date.split('/')[-1] if start_date else '2026'
    page_title = f"{name} a {comune} {year_str} | Date, Programma e Info - Sagre Grosseto"
    clean_desc = f"Tutte le informazioni su {name} a {comune} ({start_date} - {end_date}): date, programma, stand gastronomici tipici e indicazioni stradali in provincia di Grosseto.".replace('"', '&quot;')
    
    rich_program = prog if prog else f"<p>{desc}</p>"

    # Find 3-4 related events (same main comune first, then others)
    main_comune = comune.split('(')[0].strip()
    related = []
    # 1. Same municipality
    for other in events:
        if other['slug'] != slug and other['slug'] not in [r['slug'] for r in related]:
            if other.get("Comune / Frazione", "").startswith(main_comune):
                related.append(other)
                if len(related) >= 4:
                    break
    # 2. Fill with other events if fewer than 4
    if len(related) < 4:
        for offset in [1, -1, 2, -2, 3, -3, 4, 5]:
            other_idx = (idx + offset) % len(events)
            other = events[other_idx]
            if other['slug'] != slug and other['slug'] not in [r['slug'] for r in related]:
                related.append(other)
                if len(related) >= 4:
                    break

    related_cards_html = ""
    for r in related[:4]:
        r_name = r.get("Nome Evento", "")
        r_comune = r.get("Comune / Frazione", "")
        r_dates = f"{r.get('Data Inizio', '')} - {r.get('Data Fine', '')}"
        r_slug = r.get("slug", "")
        related_cards_html += f"""
                <a href="{r_slug}.html" class="p-3.5 rounded-xl border border-slate-200/80 hover:border-maremma-400 hover:bg-maremma-50/40 transition-all flex flex-col justify-between group shadow-2xs">
                    <div>
                        <h4 class="font-bold text-slate-800 text-sm group-hover:text-maremma-700 transition-colors">{r_name}</h4>
                        <p class="text-xs text-slate-500 mt-1 flex items-center gap-1"><i class="fa-solid fa-location-dot text-rose-400"></i> {r_comune}</p>
                    </div>
                    <p class="text-[11px] text-slate-400 font-semibold mt-2 pt-2 border-t border-slate-100 flex items-center justify-between">
                        <span><i class="fa-regular fa-calendar mr-1"></i>{r_dates}</span>
                        <span class="text-maremma-600 font-bold group-hover:translate-x-0.5 transition-transform">Dettagli →</span>
                    </p>
                </a>"""

    related_section_html = f"""
            <div class="mt-10 pt-8 border-t border-slate-100">
                <h3 class="text-lg md:text-xl font-bold font-serif text-slate-800 mb-3 flex items-center gap-2">
                    <i class="fa-solid fa-utensils text-[#d96b27]"></i>
                    <span>Altre Sagre ed Eventi Consigliati in Maremma</span>
                </h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {related_cards_html}
                </div>
            </div>"""

    json_ld = f"""{{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{
              "@type": "ListItem",
              "position": 1,
              "name": "Sagre Grosseto",
              "item": "{site_url}/"
            }},
            {{
              "@type": "ListItem",
              "position": 2,
              "name": "{name}",
              "item": "{page_url}"
            }}
          ]
        }},
        {{
          "@type": "Event",
          "name": "{name}",
          "description": "{desc.replace('"', '&quot;')}",
          "startDate": "{iso_start}",
          "endDate": "{iso_end}",
          "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
          "eventStatus": "https://schema.org/EventScheduled",
          "location": {{
            "@type": "Place",
            "name": "{exact_loc.replace('"', '&quot;') if exact_loc else comune.replace('"', '&quot;')}",
            "address": {{
              "@type": "PostalAddress",
              "addressLocality": "{comune.replace('"', '&quot;')}",
              "addressRegion": "Toscana",
              "addressCountry": "IT"
            }}
          }},
          "image": [
            "{site_url}/Logo.png"
          ],
          "organizer": {{
            "@type": "Organization",
            "name": "Comitato Festeggiamenti {comune.replace('"', '&quot;')}",
            "url": "{site_url}/"
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
            "name": "Comitato e Artisti Locali {comune.replace('"', '&quot;')}"
          }}
        }}
      ]
    }}"""

    full_html = html_template.format(
        title=page_title,
        description=clean_desc,
        url=page_url,
        name=name,
        location=comune,
        start_date=start_date,
        end_date=end_date,
        giorni=giorni if giorni else "Tutti i giorni dell'evento",
        exact_location=exact_loc if exact_loc else comune,
        rating=rating if rating else "Non disponibile",
        rich_program=rich_program,
        related_section=related_section_html,
        json_ld=json_ld
    )

    with open(os.path.join(out_dir, file_name), 'w', encoding='utf-8') as f_out:
        f_out.write(full_html)

    sitemap_urls.append(f"""  <url>
    <loc>{page_url}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

# Scrive sitemap.xml
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(sitemap_urls) + "\n</urlset>"

with open('sitemap.xml', 'w', encoding='utf-8') as f_sitemap:
    f_sitemap.write(sitemap_content)

print(f"Generated {len(events)} SEO static pages with internal cross-links and updated sitemap.xml.")

# --- INJECT STATIC PRE-RENDERED CARDS & INTERNAL DIRECTORY INTO index.html ---
# 1. Pre-render upcoming/current events directly inside #eventsContainer for immediate SSR/Googlebot visibility
today_dt = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
upcoming_for_ssr = []
for ev in events:
    end_str = ev.get("Data Fine", "").strip()
    try:
        end_dt = datetime.strptime(end_str, "%d/%m/%Y")
        if end_dt >= today_dt:
            upcoming_for_ssr.append(ev)
    except:
        upcoming_for_ssr.append(ev)

if not upcoming_for_ssr:
    upcoming_for_ssr = events[:24]

ssr_cards = []
for ev in upcoming_for_ssr[:36]:
    n = ev.get("Nome Evento", "")
    c = ev.get("Comune / Frazione", "")
    d_start = ev.get("Data Inizio", "")
    d_end = ev.get("Data Fine", "")
    desc = ev.get("Descrizione dell'Evento", "")
    luogo = ev.get("Luogo Esatto", "") or c
    s = ev.get("slug", "")
    date_label = d_start if d_start == d_end else f"{d_start} - {d_end}"
    ssr_cards.append(f"""            <article class="bg-white rounded-2xl border border-slate-100 shadow-sm p-5 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between text-xs text-maremma-700 font-semibold mb-2">
                        <span><i class="fa-regular fa-calendar mr-1"></i>{date_label}</span>
                        <span><i class="fa-solid fa-location-dot text-rose-500 mr-1"></i>{c}</span>
                    </div>
                    <h3 class="text-lg font-bold font-serif text-slate-800 mb-2">
                        <a href="eventi/{s}.html" class="hover:text-maremma-600 transition-colors">{n}</a>
                    </h3>
                    <p class="text-xs text-slate-600 leading-relaxed line-clamp-3 mb-3">{desc}</p>
                </div>
                <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
                    <span class="text-slate-400 truncate max-w-[65%]">{luogo}</span>
                    <a href="eventi/{s}.html" class="font-bold text-maremma-600 hover:text-maremma-800">Programma & Menu →</a>
                </div>
            </article>""")

ssr_cards_html = "\n".join(ssr_cards)

# 2. Build directory links sorted alphabetically by event name (with <details open> for full crawlability)
sorted_events = sorted(events, key=lambda x: x.get('Nome Evento', '').lower())
dir_links = []
for ev in sorted_events:
    n = ev.get('Nome Evento', '')
    c = ev.get('Comune / Frazione', '').split('(')[0].strip()
    s = ev.get('slug', '')
    dir_links.append(f'<a href="eventi/{s}.html" class="p-2 rounded-xl bg-white border border-slate-200/70 hover:border-maremma-500 hover:text-maremma-700 transition-colors flex items-center justify-between gap-1 shadow-2xs truncate" title="{n} a {c}"><span class="truncate font-medium">{n}</span><span class="text-[10px] text-slate-400 shrink-0 font-normal">{c}</span></a>')

dir_grid_html = "\n".join(dir_links)

directory_block = f"""<!-- SEO_EVENT_DIRECTORY_START -->
            <div class="pt-6 border-t border-slate-100">
                <details open class="group bg-slate-50 p-4 rounded-2xl border border-slate-200/60 cursor-pointer">
                    <summary class="font-semibold text-slate-800 list-none flex justify-between items-center text-sm sm:text-base">
                        <span class="flex items-center gap-2">
                            <i class="fa-solid fa-book-open text-maremma-600"></i>
                            <span>Tutte le {len(events)} Schede delle Sagre in Maremma (Indice A-Z)</span>
                        </span>
                        <i class="fa-solid fa-chevron-down text-slate-400 group-open:rotate-180 transition-transform"></i>
                    </summary>
                    <p class="mt-3 text-xs text-slate-500 leading-relaxed">
                        Consulta le schede informative ufficiali con date, programma dettagliato, menu gastronomico e indicazioni stradali per ciascun evento:
                    </p>
                    <div class="mt-4 pt-3 border-t border-slate-200/60 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2 text-xs">
{dir_grid_html}
                    </div>
                </details>
            </div>
            <!-- SEO_EVENT_DIRECTORY_END -->"""

if os.path.exists('index.html'):
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()

    idx_norm = idx_content.replace('\r\n', '\n')

    # Update static pre-rendered cards inside #eventsContainer
    idx_norm = re.sub(
        r'(<div id="eventsContainer"[^>]*>)(.*?)(</div>\s*<!-- Empty State -->)',
        lambda m: f"{m.group(1)}\n{ssr_cards_html}\n        {m.group(3)}",
        idx_norm,
        flags=re.DOTALL
    )

    if '<!-- SEO_EVENT_DIRECTORY_START -->' in idx_norm:
        # Replace existing directory
        idx_norm = re.sub(
            r'<!-- SEO_EVENT_DIRECTORY_START -->.*?<!-- SEO_EVENT_DIRECTORY_END -->',
            directory_block,
            idx_norm,
            flags=re.DOTALL
        )
        print("Updated SEO event directory and static SSR cards in index.html")
    else:
        insert_marker = '<hr class="border-slate-100 my-4">'
        if insert_marker in idx_norm:
            idx_norm = idx_norm.replace(insert_marker, directory_block + "\n\n            " + insert_marker, 1)
            print("Inserted SEO event directory into index.html")
        else:
            print("WARNING: insert_marker not found in index.html")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_norm)

print("Done complete SEO build and index update.")
