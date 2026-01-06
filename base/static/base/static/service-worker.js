const CACHE_NAME = "pendientes-2026-v1";

const URLS_A_CACHEAR = [
    "/",
];

// Instalar service worker
self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(URLS_A_CACHEAR);
        })
    );
});

// Activar service worker
self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(keys =>
            Promise.all(
                keys.filter(k => k !== CACHE_NAME)
                    .map(k => caches.delete(k))
            )
        )
    );
});

// Interceptar peticiones
self.addEventListener("fetch", event => {
    event.respondWith(
        fetch(event.request).catch(() =>
            caches.match(event.request)
        )
    );
});
