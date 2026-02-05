var CACHE_NAME = "nexo-pwa-v1";

var urlsToCache = [
  "/",
  "/offline/",
];

self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function (cache) {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", function (event) {
  event.respondWith(
    caches.match(event.request)
      .then(function (response) {
        return response || fetch(event.request);
      })
      .catch(() => caches.match("/offline/"))
  );
});
