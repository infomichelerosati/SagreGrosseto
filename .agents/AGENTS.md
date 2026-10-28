# Regole di Progetto per Gemini - Sagre Grosseto & Maremma

## 1. Identità e Configurazione Git
- In questo workspace usa sempre l'account github `infomichelerosati` e l'email `info.michele.rosati@gmail.com`.
- I file sorgente (HTML, CSS, JS, Python, CSV) devono essere sempre salvati in codifica **UTF-8 rigorosa** senza caratteri corrotti o mojibake (evitare token come Ã, ðŸ, â­, Âª, \ufffd).
- Ad ogni modifica a script o dati, incrementare sempre la variabile `CACHE_VERSION` in `sw.js` per aggiornare tempestivamente la Service Worker cache della PWA.
- Quando si aggiorna la directory eventi o i dati, eseguire `python build_seo_pages.py` per sincronizzare le pagine statiche e la sitemap.

## 2. Sistema Segnalazioni Utenti Anonime & Foglio Google
- **Google Sheet Master:** ID `1wMb6K1GmFs4VpjZan_E-J3S1DiNr_LNR3UVceV87GqY` (Foglio "Segnalazioni Sagre").
- **Endpoint Web App Google Apps Script:** `https://script.google.com/macros/s/AKfycbwTXtHbVDeXjRw0XjOBMb5m1uvqMKcTU55-2f6FAEK1TkO3RvoH-Qaavb0OXGh5nhgfBA/exec`
- **Frontend (`index.html`):** Nel pop-up di segnalazione anonima (`#feedbackModal`), la richiesta POST viene inviata con:
  - `method: 'POST'`
  - `mode: 'no-cors'`
  - `headers: { 'Content-Type': 'text/plain;charset=utf-8' }` (CORS-safelisted per evitare preflight)
  - `keepalive: true`
  - Un timeout `Promise.race` a 900ms per gestire il redirect 302 di Google senza bloccare il browser dell'utente e chiudere subito con notifica toast verde.

## 3. Notifiche Email Automatiche
- Le email di notifica a `info.michele.rosati@gmail.com` vengono inviate direttamente da Google Apps Script tramite `MailApp.sendEmail({ to, subject, htmlBody })` ad ogni nuova segnalazione registrata in `doPost(e)`.
- Questa soluzione nativa Google evita restrizioni su porte esterne non standard da parte del firewall Google.

## 4. Dashboard Locale di Gestione Segnalazioni
- **File:** `admin-segnalazioni.html` (apribile localmente con doppio clic su Windows).
- **Funzionalità principali:**
  - Caricamento in tempo reale tramite chiamata `doGet` all'endpoint Apps Script.
  - Raggruppamento per evento con contatore di convergenza visibile se più persone segnalano la stessa sagra.
  - Filtri: *Da Verificare*, *Solo Risolte*, *Tutte*, *Cestino (eliminate)*.
  - Gestione stato con salvataggio persistente in `localStorage` (`resolved_ids` e `deleted_ids`).
  - Funzione "Cestina Risolte" per pulizia rapida dello schermo.
  - Pulsante esportazione in Excel/CSV (`segnalazioni_sagre_YYYY-MM-DD.csv`).
  - Pulsante rapido "Apri Foglio Google" per accesso diretto al database.

## 5. Server VPS ed Ecosistema n8n
- **Host n8n:** `https://n8n.spiritoindomito.it` (protetto dietro Caddy su `127.0.0.1:5678`)
- **Workflow n8n:** ID `cNDxe4L0QaQyxTBA` ("Segnalazioni Sagre Grosseto - Notifica Email").
- Il server MCP e l'API di n8n sono predisposti qualora si desideri espandere il flusso verso notifiche push Telegram, bot WhatsApp o database esterni.

## 6. Fonti di Riferimento per Ricerca Eventi e Sagre (100% Gratuiti)
- **Virgilio Eventi Grosseto:** `https://www.virgilio.it/italia/grosseto/eventi/` (calendario mensile con mercatini, mostre, antiquariato e manifestazioni cittadine).
- **Sagre Toscane:** `https://www.sagretoscane.com/` (portale principe per sagre enogastronomiche, stand aperti e menu tipici).
- **TuttoMaremma & Maremma.name:** `https://www.tuttomaremma.com/` (feste popolari, riti del fuoco e tradizioni dei borghi).
- **Testate Locali della Maremma:** `https://www.ilgiunco.net/`, `https://www.maremmaoggi.net/`, `https://www.grossetonotizie.com/`.
- **Canali Istituzionali:** Siti ufficiali dei 28 Comuni della provincia di Grosseto, pagine ufficiali Pro Loco e `https://www.visittuscany.com/`.
- **Criterio vincolante:** Includere solo manifestazioni ad accesso libero e gratuito per il pubblico.
