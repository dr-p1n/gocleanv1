// Cloudflare Pages Function — manejo de rutas spam.
//
// Contexto: el sitio es 100% estatico y NO tenia Worker ni Functions. Este es el
// primer archivo de `functions/`, asi que a partir de aqui el proyecto deja de ser
// Pages puro: toda peticion pasa por este middleware antes de llegar al servidor
// de assets. Se escribe para ser lo mas barato posible — un test de regex sobre el
// pathname y, si no hay coincidencia, `context.next()` sin tocar nada.
//
// Que hace: devuelve 410 Gone con `X-Robots-Tag: noindex` para los patrones de URL
// basura que los crawlers siguen pidiendo. Esas rutas YA devolvian 404 (verificado
// en produccion el 2026-11-04); el 410 es una senal mas fuerte y definitiva que el
// 404, asi que Google las retira del indice antes y deja de reintentarlas.
//
// Verificado antes de escribir esto: ninguna de las 72 URLs del sitemap, y ningun
// enlace interno del sitio, casa con estos patrones. Si algun dia se anade una
// pagina real bajo /search o /product/..., hay que quitar la regla correspondiente.
const SPAM_PATTERNS = [
  // Rutas de spam observadas en los logs de rastreo.
  /^\/pcmypage/i,
  /^\/safe_search\//i,
  /^\/zhHant\//i,
  // RETIRADAS A PROPOSITO — no reactivar sin revisar el ecommerce:
  //   /\/product\/(detail|review)\//i
  //   /^\/search$/i
  // El ecommerce previsto para diciembre de 2026 va a crear rutas reales bajo
  // /product/... y lo mas probable es que tambien un /search. Con esas dos reglas
  // activas, las fichas de producto y el buscador devolverian 410 Gone el dia del
  // lanzamiento, y el sintoma seria dificil de rastrear hasta aqui. Las tres reglas
  // que quedan son cadenas que ningun ecommerce va a generar.
];

export async function onRequest(context) {
  const { pathname } = new URL(context.request.url);

  if (SPAM_PATTERNS.some((pattern) => pattern.test(pathname))) {
    return new Response("410 Gone\n", {
      status: 410,
      headers: {
        "Content-Type": "text/plain; charset=utf-8",
        // Explicito en la respuesta: la regla `/*` de `_headers` declara
        // `index, follow` y aplica al servidor de assets, no a lo que devuelve
        // una Function. Sin esta linea la respuesta saldria sin directiva.
        "X-Robots-Tag": "noindex",
        // Cacheable: son rutas muertas, no hace falta recalcularlas en cada hit.
        "Cache-Control": "public, max-age=86400",
      },
    });
  }

  // Todo lo demas sigue su curso normal: _redirects, _headers, las paginas
  // estaticas y el 404.html real para rutas desconocidas.
  return context.next();
}
