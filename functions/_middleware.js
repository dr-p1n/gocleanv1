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
  // Restos del sitio viejo (informes de Search Console del 2026-11-04: ~1.000
  // "No encontrada (404)" + 4.558 "Rastreada: sin indexar", todo basura estilo
  // catalogo japones). Se acotan a la FORMA exacta observada, no a rutas amplias:
  //   /738555802            raiz con 8-9 digitos y nada mas (744 de 1.000 muestras)
  //   /items/088007924.html catalogo con id numerico (?srsltid=... irrelevante)
  // Riesgo asumido y revisable: si el ecommerce usara ids numericos de 8+ digitos
  // directamente en la raiz, esta regla los mataria. Avisar al equipo de la tienda.
  /^\/\d{8,}$/,
  /^\/items\/\d+\.html$/i,
  // RETIRADAS A PROPOSITO — no reactivar sin revisar el ecommerce:
  //   /\/product\/(detail|review)\//i
  //   /^\/search$/i   (solo la variante con firma de spam se mata; ver isSpamSearch)
  // El ecommerce previsto para diciembre de 2026 va a crear rutas reales bajo
  // /product/... y lo mas probable es que tambien un /search. Con esas dos reglas
  // activas, las fichas de producto y el buscador devolverian 410 Gone el dia del
  // lanzamiento, y el sintoma seria dificil de rastrear hasta aqui. Las tres reglas
  // que quedan son cadenas que ningun ecommerce va a generar.
];

// /search NO esta en SPAM_PATTERNS a proposito: el ecommerce de diciembre puede
// tener un buscador real ahi. El spam del sitio viejo, en cambio, es inconfundible:
// `/search?category&search_word&restrict[]=person_id(int)=XXXX` (100 de 100 en el
// export). Se mata SOLO cuando la query trae esa firma; `/search`, `/search?q=...`
// y cualquier parametro de buscador legitimo siguen su curso.
function isSpamSearch(url) {
  if (url.pathname !== "/search") return false;
  let query = url.search;
  try {
    query = decodeURIComponent(url.search.replace(/\+/g, " "));
  } catch (_) {
    // Percent-encoding malformado: se evalua la query cruda. Nunca debe lanzar,
    // porque este middleware corre antes que todo el sitio.
  }
  return /person_id\(int\)/i.test(query) && /search_word/i.test(query);
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const { pathname } = url;

  if (isSpamSearch(url) || SPAM_PATTERNS.some((pattern) => pattern.test(pathname))) {
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
  const response = await context.next();

  // Correccion del X-Robots-Tag en las respuestas 404.
  //
  // El problema: la regla `/*` de `_headers` declara `index, follow, ...` y se
  // aplica por RUTA DE PETICION, no por codigo de respuesta. Una ruta inexistente
  // casa con `/*`, asi que el 404 salia con `X-Robots-Tag: index, follow` mientras
  // el propio 404.html lleva `<meta name="robots" content="noindex, follow">`:
  // dos senales contradictorias en la misma respuesta.
  //
  // Por que NO se arregla en `_headers` (corrige la nota de v9): el fichero solo
  // sabe casar patrones de URL — no existe condicion por status. Y una regla
  // `/404.html` solo cubriria una peticion literal a /404.html, no las rutas
  // desconocidas que son justo las que devuelven el 404. Verificado contra la
  // documentacion de Pages el 2026-11-04.
  //
  // Aqui si se puede porque el middleware ya ve la respuesta montada. Se clona
  // para poder escribir las cabeceras (las de `context.next()` son inmutables) y
  // se alinea el header con el meta de la pagina.
  if (response.status === 404) {
    const patched = new Response(response.body, response);
    patched.headers.set("X-Robots-Tag", "noindex, follow");
    return patched;
  }

  return response;
}
