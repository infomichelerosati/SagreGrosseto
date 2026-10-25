// Service Worker per Sagre Grosseto e Maremma
// Strategia "Auto-Updating": Network-First per dati e HTML, per evitare cache bloccate
const CACHE_VERSION = 'sagre-v1.3.3-20261025';
const STATIC_CACHE = `${CACHE_VERSION}-static`;
const DATA_CACHE = `${CACHE_VERSION}-data`;

// Risorse statiche core essenziali per l'avvio offline
const PRECACHE_ASSETS = [
    '/',
    '/index.html',
    '/manifest.json',
    '/Logo.png',
    '/icons/icon-192x192.png',
    '/icons/icon-512x512.png',
    '/icons/apple-touch-icon.png'
];

// 1. Installazione: forza l'attivazione immediata senza attendere chiusura tab
self.addEventListener('install', (event) => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(STATIC_CACHE).then((cache) => {
            return cache.addAll(PRECACHE_ASSETS).catch((err) => {
                console.warn('Errore pre-cache non bloccante:', err);
            });
        })
    );
});

// 2. Attivazione: elimina subito tutte le vecchie cache e prende il controllo
self.addEventListener('activate', (event) => {
    event.waitUntil(
        Promise.all([
            // Cancella tutte le cache di versioni precedenti
            caches.keys().then((keys) => {
                return Promise.all(
                    keys.map((key) => {
                        if (key !== STATIC_CACHE && key !== DATA_CACHE) {
                            console.log('[SW] Rimozione vecchia cache:', key);
                            return caches.delete(key);
                        }
                    })
                );
            }),
            // Prendi il controllo immediato di tutte le schede aperte
            self.clients.claim()
        ])
    );
});

// 3. Fetch: Strategia differenziata intelligente
self.addEventListener('fetch', (event) => {
    const request = event.request;
    const url = new URL(request.url);

    // Ignora richieste non GET o estensioni browser
    if (request.method !== 'GET' || !url.protocol.startsWith('http')) {
        return;
    }

    // A) HTML di navigazione e CSV dati: NETWORK-FIRST con fallback su Cache
    // In questo modo, finché l'utente è online, riceve SEMPRE la versione più recente
    const isNavigation = request.mode === 'navigate';
    const isDataOrHTML = url.pathname.endsWith('.csv') || url.pathname.endsWith('.html') || url.pathname === '/';

    if (isNavigation || isDataOrHTML) {
        event.respondWith(
            fetch(request)
                .then((networkResponse) => {
                    // Se la risposta è valida, aggiorna la cache in background
                    if (networkResponse && networkResponse.status === 200) {
                        const responseClone = networkResponse.clone();
                        caches.open(isDataOrHTML ? DATA_CACHE : STATIC_CACHE).then((cache) => {
                            cache.put(request, responseClone);
                        });
                    }
                    return networkResponse;
                })
                .catch(() => {
                    // Se siamo offline o c'è errore di rete, usa la versione in cache
                    return caches.match(request).then((cachedResponse) => {
                        if (cachedResponse) return cachedResponse;
                        // Fallback per navigazione offline
                        if (isNavigation) return caches.match('/index.html');
                        return new Response('Offline: contenuto non disponibile', { status: 503 });
                    });
                })
        );
        return;
    }

    // B) Risorse statiche (Immagini, Icone, Font, Script CDN): CACHE-FIRST con revalidazione
    event.respondWith(
        caches.match(request).then((cachedResponse) => {
            if (cachedResponse) {
                // Ritorna subito la risorsa in cache per massima velocità
                // e aggiorna in background (Stale-While-Revalidate)
                fetch(request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        caches.open(STATIC_CACHE).then((cache) => cache.put(request, networkResponse));
                    }
                }).catch(() => {/* offline silente */});
                return cachedResponse;
            }

            // Se non è in cache, scarica dalla rete e memorizza
            return fetch(request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                    const responseClone = networkResponse.clone();
                    caches.open(STATIC_CACHE).then((cache) => {
                        cache.put(request, responseClone);
                    });
                }
                return networkResponse;
            });
        })
    );
});
