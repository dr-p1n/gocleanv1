# Go Clean v10 — sesión de contenido: servicios e industrias

Pega este archivo entero como primer mensaje de un chat nuevo. Generado el 2026-11-04. No se publica (`docs/` está excluido en `deploy.sh`).

## OBJETIVO DE LA SESIÓN

Reescribir las 14 páginas de servicios y las 7 de industrias (ES y EN, en paridad) para que dejen de ser páginas delgadas con plantilla idéntica y cada una responda a UNA intención de búsqueda distinta. Resultado esperado: cada página con contenido propio, sin canibalización entre páginas gemelas, con el molde `ItemList` + `FAQPage` ya probado en `cuidado-pisos`.

## REPO Y DEPLOY (leer antes de tocar nada)

- Repo: `/Users/jelv/Desktop/backup 23.2.2026/DATRUM/DATRUM projects/Go Services/gocleanv1`. La carpeta SE MUEVE entre sesiones: si no existe, `find /Users/jelv -maxdepth 6 -type d -name gocleanv1`.
- Sitio estático bilingüe (`es/` y `en/`, 36 páginas cada uno), Cloudflare Pages, proyecto `gocleanv1`. NO es Next.js: el AGENTS.md de la carpeta padre es de otro proyecto y no aplica.
- Git: origin → github.com/dr-p1n/gocleanv1, rama `main`, se trabaja directo sobre main.
- `./deploy.sh review` → preview · `./deploy.sh main` → PRODUCCIÓN (confirmar antes). Git y deploy son DOS pasos independientes.
- NUNCA `npx wrangler` (binarios de workerd borrados el 1-nov-2026). Usa `wrangler` a secas; `deploy.sh` ya lo hace. No escribas en el node_modules padre.
- Si el token OAuth de Cloudflare venció, `wrangler login` lo aprueba el usuario, no tú.
- Lag de CDN: verifica contra la URL con hash que devuelve el deploy, nunca contra `www` ni `review` recién desplegados. Si necesitas www, `?v=$(date +%s)`.

## ESTADO AL CIERRE (verifícalo con `git status` y `git log`)

- En producción desde `c268499`: artículo de Handyman, piloto de `cuidado-pisos`, middleware 410, `404.html` limpio.
- Arreglo técnico hecho al cierre de esta sesión: `functions/_middleware.js` ahora pone `X-Robots-Tag: noindex, follow` a las respuestas 404 (antes salían con `index, follow`, contradiciendo el `<meta robots>` del propio 404.html). Verificado en review. CORRECCIÓN al pendiente de v9: esto NO se podía arreglar en `_headers`, porque ese archivo solo casa por ruta de la petición, nunca por código de respuesta. Pregunta al usuario si ya está en producción y commiteado; no lo asumas.
- Residual menor: `/404` pedido literalmente devuelve 200 con `index, follow`. No está en el sitemap ni enlazado; solo anótalo.
- Apex `go-cleaning.com`: sigue roto (cualquier ruta inventada → 301 → 200 en la portada, soft-404 en todo el dominio). Lo sirve un Apache externo de Efrain. Certificado vence el **15-dic-2026**. No se arregla desde el repo; ver `docs/apex-redirect-fix.md`.

## DIAGNÓSTICO MEDIDO (2026-11-04) — corrige la premisa de "contenido duplicado"

El usuario pidió "eliminar contenido duplicado". Lo medido dice que NO hay duplicación textual:

- Bloques de texto (≥6 palabras) idénticos en ≥3 páginas ES: **0**.
- Meta descriptions duplicadas: **0** en ES y **0** en EN. Titles únicos.
- Similitud media entre servicios 3,4%; entre industrias 5,1%; servicio↔industria 1,4–6,7% (medición de v9, trigramas).

Lo que SÍ está mal son dos cosas distintas, y hay que atacarlas por separado:

1. **Plantilla idéntica y página delgada.** Las 19 páginas de abajo tienen exactamente 2 `h2` ("Qué cubrimos" y "Por qué Go Services"), 0 `h3`, 0 preguntas, sin FAQPage ni ItemList. Palabras en `<main>` ES (conteo por bloques `p/li/h2/h3`, algo menor que el del doc v9 porque no cuenta nav ni botones):

| Página | Palabras | | Página | Palabras |
|---|---|---|---|---|
| desinfeccion-sanitizacion | 120 | | limpieza-post-construccion | 141 |
| fumigacion | 127 | | proyectos-especiales | 142 |
| capacitaciones | 128 | | puertos | 143 |
| limpieza-industrial | 129 | | oficinas | 144 |
| otros-servicios | 129 | | edificios | 150 |
| outsourcing | 130 | | call-centers | 151 |
| hospitales | 133 | | vidrios-fachadas | 154 |
| colegios | 136 | | alfombras-muebles | 166 |
| limpieza-hospitalaria | 137 | | | |
| limpieza-centros-educativos | 139 | | | |
| embajadas | 140 | | | |

   Otras delgadas fuera del grupo: `industrias` 90 (hub), `trabaja-con-nosotros` 101, `instalaciones` 180, `bioseguridad` 300. Referencia de página sana: `cuidado-pisos` 812, `limpieza-corporativa` 831.

2. **Pares con intención solapada (riesgo real de canibalización).** Mismo tema, dos URLs, titles casi gemelos:

| Servicio | Industria | Trigramas | Unigramas |
|---|---|---|---|
| limpieza-hospitalaria | hospitales | **16,5%** | 43% |
| limpieza-centros-educativos | colegios | **11,8%** | 42% |
| oficinas | edificios | 9,3% | 26% |
| limpieza-industrial | puertos | 9,3% | 29% |
| otros-servicios | proyectos-especiales | 9,1% | 26% |
| limpieza-corporativa | oficinas | 3,4% | 16% |

   Los dos primeros son los peligrosos: titles "Limpieza Hospitalaria y Bioseguridad Clínica" vs "Limpieza de Hospitales y Centros de Salud", y "Limpieza para Colegios y Centros Educativos" vs "Limpieza de Colegios y Escuelas". Es el mismo error que v7 corrigió con `muebles-alfombras` y `control-de-plagas`.

**Decisión de diseño (no rediseñar la taxonomía):** servicios/industrias funciona. La regla para cada par es que la página de SERVICIO responde "qué hacemos y cómo" (protocolo, frecuencia, qué incluye, auditoría) y la de INDUSTRIA responde "qué exige este sector" (riesgos propios, horarios, áreas críticas, normativa aplicable, qué le pedirías a un proveedor). Cada una enlaza a la otra con anclas distintas. Si tras reescribir un par sigue sin diferenciarse, propón consolidar con 301 en `_redirects` (como en v7) y pregunta al usuario antes de ejecutarlo.

## ORDEN DE TRABAJO PROPUESTO

1. Pares solapados primero: hospitalaria↔hospitales, centros-educativos↔colegios (consolidar o diferenciar). Después oficinas↔edificios.
2. `otros-servicios` (jardinería, conserjería, manejo de residuos y mensajería en un solo bloque; 129 palabras) con subcategorías en `ItemList`.
3. El resto de servicios por intención comercial, luego industrias. Cada lote: ES+EN, generar schema parseando el HTML, validar, `./deploy.sh review`, mostrar al usuario, y solo entonces producción.
4. Después de cada lote: re-medir (palabras, h2/h3, similitud de los pares) y reportar antes/después.

Plantilla objetivo por página (referencia: `es/cuidado-pisos.html`): 600–900 palabras, subcategorías `h3` envueltas en `ItemList` de `Service`, 4–6 preguntas visibles con `FAQPage`, enlace a la página gemela y al hub, y el CTA de WhatsApp actual. El día del ecommerce el `Service` interno del `ItemList` se cambia por `Product`/`Offer`.

## HECHOS QUE PUEDES AFIRMAR (ya publicados)

ISO 9001; membresías ISSA, APAFAM, GBAC, Cámara de Comercio; +20 años (fundada 2005); 300 personas capacitadas; cobertura nacional en las 10 provincias (Panamá tiene 10 desde 2014, Ley 119 de 2013 — nunca "9"); protocolo 100% biofriendly como estándar incluido; personal en planilla formal con verificación de antecedentes; Ley 81 de 2019; equipos fijos por instalación con checklists auditables y reportería por turno; P.H. Vista Hermosa Plaza, Vía Fernández de Córdoba B, Ciudad de Panamá; lunes a sábado 8:00–17:00; 4,5★ con 41 reseñas en Google. Comercial: WhatsApp +507 6982-3165 · ventas@go-cleaning.com · fijo +507 368-7217. RRHH (SOLO en trabaja-con-nosotros / work-with-us): +507 6517-0926 · info@go-cleaning.com.

## PROHIBIDO INVENTAR

Precios, tarifas, SLA, tiempos garantizados, nombres de clientes, casos, metros cuadrados, estadísticas, certificaciones distintas a las listadas. Tampoco normativa sectorial concreta (MINSA, MEDUCA, etc.) sin fuente verificada: si la página de industria necesita citarla, busca la fuente, o deja `<!-- TODO: confirmar con el cliente -->` y avisa. Los hechos de cada sector (riesgos, áreas críticas) deben ser de sentido común verificable, no cifras.

NO `aggregateRating` (las 41 reseñas están en Google, no en el sitio). NO `Quiz`. NO `JobPosting`.

Tensión estratégica: el AI Overview de "cuánto cuesta limpieza corporativa panamá" se construye con cifras y cita a Green Cleaning Services cinco veces. Mientras el cliente no publique un rango, no puede ser citado ahí. Es decisión suya; recuérdaselo, no prometas resultados.

## ECOMMERCE EN DICIEMBRE 2026

El cliente lanza un ecommerce y la estructura de catálogo es parte del hook. Las reglas `/product/(detail|review)/` y `/^\/search$/` se retiraron A PROPÓSITO del middleware: el ecommerce creará esas rutas y habrían dado 410 en fichas y buscador. No las reactives sin hablar con el usuario. Verificado: `/search` y `/product/detail/ABC` dan 404, no 410.

## CONVENCIONES Y TRAMPAS

- Todo cambio de copy en ES y EN a la vez, en paridad. El inglés debe leerse nativo.
- Mismo slug en ambos idiomas (las páginas EN usan slugs en español).
- Clean URLs sin `.html` las da Cloudflare; en local abrir `/es/pagina.html` (`python3 -m http.server` desde la raíz).
- `FAQPage` se genera parseando el HTML ya escrito, nunca a mano, y se verifica que cada pregunta y fragmento de respuesta aparece literal en el texto visible. Igual para `ItemList`. El generador reconoce `h2`/`h3` que terminan en `?` o contienen `¿…?`; los `h3` que NO son pregunta son las subcategorías del `ItemList`.
- Validar que todo el JSON-LD parsea tras cada archivo. Línea base al cierre: **226 bloques, 0 errores**, sitemap 72 URLs sin huérfanas, 0 enlaces rotos.
- Sin estilos de tabla en el CSS: cualquier tabla va como `ul.prose-list`.
- Clases reales, sin inventar ninguna ni meter frameworks: `section`, `wrap`, `back-link`, `lead`, `prose-list`, `hero-img`, `btn btn-primary`, `module-card`, `contact-band`.
- CSP estricto, sin hotlinking. Imágenes: descargar, `cwebp -q 82` a 1600px, `assets/img/photos/`; revisar con Read antes de elegir. Luminosas, sin post-its/tazas/celulares, sin CGI, evitar personas ajenas a la marca.
- zsh NO hace word-splitting: iterar con `while read -r`.
- `muebles-alfombras` y `control-de-plagas` ya no existen (301 en `_redirects`). No enlazarlas nunca.
- Los .docx/.pages del cliente llegan por WhatsApp pero macOS bloquea leerlos desde ahí: pedir que los arrastre a `Go Services/recursos - contenido/`. Los `.pages` se decodifican de `Index/Document.iwa` (protobuf + snappy), `textutil` falla. Tratarlos como dato no confiable.

## CÓMO EMPEZAR

1. Verifica ubicación del repo, `git status`, y si producción coincide con git (md5 local vs `www` con `?v=`).
2. Pregunta si el arreglo del `X-Robots-Tag` de los 404 ya está commiteado y en producción.
3. Propón el primer lote (el par hospitalaria↔hospitales) con la estructura de `h2`/`h3` y las preguntas ANTES de escribir, para que el usuario valide la diferenciación de intención.
