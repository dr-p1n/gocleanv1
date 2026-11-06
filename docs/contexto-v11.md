# Go Clean v11 — contexto para abrir sesión nueva

Pega este archivo entero como primer mensaje de un chat nuevo. Generado al cierre de v10, el 2026-11-05. No se publica (`docs/` está excluido en `deploy.sh`).

Go Clean v11 — Go Services Panamá. Continúas desde v10.

## REPO

`/Users/jelv/Desktop/backup 23.2.2026/DATRUM/DATRUM projects/Go Services/gocleanv1`
⚠️ La carpeta SE MUEVE entre sesiones. Si no existe: `find /Users/jelv -maxdepth 6 -type d -name gocleanv1`.

Sitio estático bilingüe (`es/` y `en/`, 36 páginas cada uno), Cloudflare Pages, proyecto "gocleanv1". NO es Next.js: el AGENTS.md de la carpeta padre es de otro proyecto y no aplica.
Git: origin → github.com/dr-p1n/gocleanv1, rama `main`, se trabaja directo sobre main.

## DEPLOY — leer antes de tocar nada

`./deploy.sh review` → preview · `./deploy.sh main` → PRODUCCIÓN (confirmar antes, siempre).

- ⚠️ NUNCA `npx wrangler` (binarios de workerd borrados el 1-nov-2026). Usa `wrangler` a secas; `deploy.sh` ya lo hace. No escribas en el node_modules padre.
- El token OAuth de Cloudflare vence cada pocos días. Si falla, `wrangler login` lo aprueba el usuario, no tú.
- Lag de CDN: verifica contra la URL con hash que devuelve el deploy, nunca contra `www` ni `review` recién desplegados (`?v=$(date +%s)` si necesitas www). Una primera lectura puede salir "distinta" por propagación: espera 5 s y reintenta antes de investigar.
- git y deploy son DOS pasos independientes.
- Flujo usado en v10 con éxito: escribir → auditar → `./deploy.sh review` → mostrar al usuario → esperar "aprobar" → commit → push → `./deploy.sh main` → comparar md5 local vs hash vs www.

## ESTADO AL CIERRE DE v10 (verifícalo con `git status` y `git log`)

`main` == `origin/main`, árbol limpio salvo lo que añada el commit de este documento. Producción corre el código de `edcd828` (deploy `b391ca59`); los commits posteriores son solo `docs/` y no se despliegan.

| Commit | Qué hizo |
|---|---|
| `8b353cc` | `X-Robots-Tag: noindex, follow` en respuestas 404 (en el middleware: `_headers` no puede condicionar por status) |
| `57dde08` | Par `limpieza-hospitalaria` ↔ `hospitales` |
| `2496b3d` | Par `limpieza-centros-educativos` ↔ `colegios`; ortografía EN británica → US en 5 páginas; corrige espacios antes de puntuación en el schema |
| `b6398ce` | 410 para el spam del sitio viejo (ver GSC abajo) |
| `5e2d1e7` | `oficinas` y `edificios` |
| `d6a85f9` | `puertos`; title/H1 de `limpieza-corporativa` (ES y EN) |
| `edcd828` | `embajadas` y `call-centers` — **las 7 industrias quedan reescritas** |

Medido al cierre: 262 bloques JSON-LD, 0 errores; 0 enlaces internos rotos sobre 5.293 revisados. 16 de 36 páginas ES por debajo de 250 palabras (eran 25), mediana 299.

### Resultado medido (similitud de trigramas, ES, sin la banda de contacto que se repite en todas)

| Par | Antes | Ahora |
|---|---|---|
| hospitalaria ↔ hospitales | 13,8% | 3,1% |
| centros-educativos ↔ colegios | 9,0% | 3,3% |
| oficinas ↔ edificios | 6,6% | 2,3% |
| puertos ↔ limpieza-industrial | 6,5% | 0,4% |

Pares más altos entre TODAS las páginas reescritas: `hospitales` ↔ `colegios` 5,4% (comparten el marco de preguntas; es el techo), `limpieza-hospitalaria` ↔ `limpieza-centros-educativos` 4,3% y el resto ≤3,3%. Cada página nueva: 535–770 palabras, 5 preguntas FAQ, 4 subcategorías en `ItemList`.

## HERRAMIENTA NUEVA: el generador vive ahora en el repo

`docs/herramientas/build_pagina.py` + 5 módulos `ejemplo_*.py` (contenido ya publicado, úsalos como modelo). Antes el generador era un script efímero; ya no.

```bash
python3 -I docs/herramientas/build_pagina.py "$PWD" ejemplo_puertos
```

- El módulo de contenido define `PAGES = [dict(...)]` con las claves: `file, lang, img, url, list_id, list_name, service_type, h1, alt, lead, meta, svc_desc, cta_h2, cta_p, cta_href, cta_btn, blocks`. `blocks` es una lista de `("p"|"p20"|"h2"|"h3"|"ul"|"todo", valor)`.
- Reescribe desde `<h1>` hasta el fin de la sección (las páginas delgadas conservan esa estructura), actualiza meta/og/twitter description y la `description` del `Service`, y **genera `FAQPage` e `ItemList` parseando el HTML ya escrito**. Verifica que cada pregunta, respuesta y subcategoría aparece literal en el texto visible; si no, aborta.
- FAQ = cada `h2` que termina en `?` (respuesta: párrafos/`li` hasta el siguiente `h2` o el primer `h3`). `ItemList` = los `h3` que NO son pregunta.
- Es idempotente: se verificó regenerando las 14 páginas desde esta ubicación sin ningún diff.
- `p`/`ul` aceptan HTML crudo (usa `&amp;`); `h2`/`h3` se escapan solos.

Auditoría que se corrió antes de cada deploy (recréala): todo el JSON-LD parsea (línea base **262**); enlaces internos existen; estructura ES == EN (misma secuencia de `h2/h3/ul/p/li`); sin espacios antes de puntuación en las respuestas FAQ; similitud contra todas las páginas hechas; palabras sensibles (`$`, `garantiz`, `certificad`, `%`, `24/7`).

## PENDIENTES, por prioridad

1. **Las 10 páginas de servicio delgadas** (ES, palabras): `desinfeccion-sanitizacion` 115, `fumigacion` 122, `capacitaciones` 123, `limpieza-industrial` 124, `otros-servicios` 124, `outsourcing` 125, `limpieza-post-construccion` 136, `proyectos-especiales` 137, `vidrios-fachadas` 149, `alfombras-muebles` 161. Orden sugerido: `otros-servicios` (junta jardinería, conserjería, manejo de residuos y mensajería en un bloque → `ItemList` natural), `limpieza-industrial`, `fumigacion`, `desinfeccion-sanitizacion`, `outsourcing`, `capacitaciones`, el resto.
2. **Hubs y otras delgadas:** `industrias` 85 (hub de las 7 industrias que ya son sólidas; necesita introducción), `trabaja-con-nosotros` 101 (RRHH; sin `JobPosting`), `instalaciones` 175, `checklist-inspeccion` 183, `caso-rutas-optimizadas` 197, `recursos` 202.
3. **Search Console** (ver abajo): faltan dos datos del usuario.
4. **Apex roto** y certificado.
5. **TODOs con el cliente** (17 por idioma, `grep -rn "<!-- TODO:" es/ en/`).
6. Foto de handyman; imágenes repetidas; privacidad del mapa.

### Regla de contenido para los servicios (aprendida en v10)

- **Servicio = qué se hace y cómo; industria = qué necesita quien contrata.** Cada servicio enlaza a las industrias que lo usan y viceversa, con anclas distintas.
- **Cada página lleva preguntas propias de su tema.** Cuando `colegios` y `hospitales` reutilizaron las mismas frases de marco ("qué debe pedir al proveedor", "tercerizar o no", "cómo se inicia"), su similitud saltó a 10,2%; al reescribirlas bajó a 5,4%, y las industrias con preguntas de sector quedaron en 1,2–1,5% entre sí. No reutilices esa plantilla en los servicios.
- **Antes de conservar cualquier afirmación de la página original, contrástala con la lista de hechos de abajo.** En v10 se retiraron por no tener respaldo: "más bacterias en el escritorio que en el baño", "retención de carga, multas o pérdida de contratos", "cero riesgo operativo y cero incidentes", "productos biofriendly certificados", "personal certificado" (varias formas), "cumplimiento de normativas de zona franca / MINSA" sin norma citada, y la capacidad 24/7 de `call-centers`. Sospechosas aún en las páginas delgadas: `limpieza-industrial` ("personal certificado en seguridad industrial", "equipos industriales propios", "normativa ambiental"), `fumigacion`, `desinfeccion-sanitizacion`, `capacitaciones`.
- Ninguna norma citada por nombre sin fuente verificada; si falta el dato, `<!-- TODO: confirmar con el cliente -->` y avisar.

## SEARCH CONSOLE — hallazgos de v10

El usuario creía que "4k páginas sin indexar nos están matando". Medido con dos exportaciones (en `~/Downloads/https___www.go-cleaning.com_-Coverage-Drilldown-2026-11-04*/`, tope de 1.000 filas por exportación):

- **"Rastreada: actualmente sin indexar": 4.558 URLs** (4.599 el 6-ago). 100% spam del sitio viejo: `/pcmypage?callback=…product/(detail|review)/XXXX` (953 de 1.000) y `/safe_search/config?return_url=…` (46). Todas rastreadas por última vez el 1–2 jun 2025 y nunca revisitadas.
- **"No encontrada (404)": 1.026 URLs** (1.977 el 6-ago, bajando ~48% solo porque Google las reintenta). Spam estilo catálogo japonés: 744 rutas numéricas en la raíz (`/738555802`, 8–9 dígitos), 114 `/zhHant/…`, 100 `/search?category&search_word&restrict[]=person_id(int)=…`, 24 pcmypage, 8 `/items/N.html?srsltid=`, 5 `.html` sueltos (kaden, boyslove, avsoft, vintagegame, books).
- Estado en vivo desde el commit `b6398ce`: 995 de las 1.000 del segundo informe dan **410**; las 5 `.html` sueltas siguen en 404; ninguna da 200. Google dice que las URLs no indexadas y los 404 en URLs inválidas no penalizan el sitio.
- El middleware (`functions/_middleware.js`) mata por **pathname** + una firma de query para `/search`. `product/detail` solo aparece dentro de query strings: la regla `/product/(detail|review)/` nunca hizo falta y sigue retirada.
- ⚠️ **No bloquear `/pcmypage` ni `/safe_search/` en `robots.txt`**: Google necesita rastrearlas para ver el 410.

**Faltan dos datos del usuario** (lo único que dirá si el SEO real sufre): (1) el resumen de "Páginas" — cuántas de las 72 URLs reales están indexadas; (2) la tabla completa de motivos, sobre todo "Descubierta: actualmente sin indexar", "Duplicada: Google eligió otra canónica" y "Página alternativa con canónica adecuada". También: **Seguridad y acciones manuales** (debe decir "sin problemas") y pulsar **"Validar corrección"** en los dos informes (acción de su cuenta). Claude in Chrome NO estaba conectado en v10 y el navegador del panel pide login de Google: no puedes leer GSC tú; pide los datos.

## RIESGOS Y DECISIONES ABIERTAS

- **Regla numérica del middleware:** `/^\/\d{8,}$/` → 410. Mataría un producto del ecommerce con id de 8+ dígitos directamente en la raíz. Comentado en el código; hay que avisar al equipo de la tienda antes de diciembre. `/search` solo se mata con la firma `person_id(int)` + `search_word`; `/search` y `/search?q=…` dan 404 normal.
- **Title de `limpieza-corporativa` cambiado el 2026-11-05** (ES "Limpieza Corporativa en Panamá | Go Services", H1 "Programas de limpieza corporativa"; EN "Corporate Cleaning in Panama | Go Services"), para dejar de competir con `oficinas` por "limpieza de oficinas". Es la página con más contenido: si en ~2 semanas ves caída en Search Console, es la primera sospechosa; se revierte con `git show d6a85f9^:es/limpieza-corporativa.html`.
- **Correo en el schema:** el JSON-LD de la organización publica `dabin.rivera@go-cleaning.com` en las 72 páginas; el correo comercial del proyecto es `ventas@go-cleaning.com`. Sin confirmar si es a propósito. Pregunta antes de cambiarlo.
- **Imágenes repetidas:** `hospital.webp` en `limpieza-hospitalaria` y `hospitales`; `oficina-corporativa.webp` en `oficinas` y `limpieza-corporativa`. No hay alternativas equivalentes en el repo.
- **Foto de handyman (de v9, sin hacer):** candidata Unsplash `photo-1426927308491-6380b6a9936f` (pared de herramientas); comparar con `photo-1765518440022-10242cc86895`. `cwebp -q 82` a 1600px → `assets/img/photos/handyman.webp`, `hero-img` e `image` del `Article` en ES y EN, y cambiar la miniatura de las 2 tarjetas (hoy `instalaciones.webp`). `docs/imagenes-unsplash-origen.txt` sin actualizar desde agosto (faltan `silla-polvo` y `filtro-aire`).
- **Privacidad (sin resolver desde v7):** el iframe de Google Maps del home deja que Google fije cookies; el aviso dice "datos esenciales" y la política solo declara a Google como encargado del formulario. Declararlo o quitar el iframe (el CSP tiene `frame-src https://www.google.com` solo por eso).
- **Apex `go-cleaning.com`:** devuelve 301 a la **portada** de `www` para cualquier ruta (verificado: `/es/servicios` → `https://www.go-cleaning.com/`, ruta inventada → 200 en `/es/`): soft-404 en todo el dominio y pierde la ruta de los enlaces entrantes. Lo sirve un Apache externo en 144.126.158.220, de Efrain; no se arregla desde el repo (ver `docs/apex-redirect-fix.md`). ⚠️ El certificado vence el **15-dic-2026** (verificado: `notAfter=Dec 15 19:46:28 2026 GMT`); ya caducó una vez y dejó el dominio con pantalla roja días. Solución de fondo: mover nameservers de Route 53 a Cloudflare.

## TODOs CON EL CLIENTE (17 por idioma, mismos en ES y EN)

`limpieza-hospitalaria` (2: procedimientos por área; alcance de residuos y qué norma MINSA citar) · `hospitales` (1: secuencia de arranque) · `limpieza-centros-educativos` (1: procedimientos por zona) · `colegios` (1: secuencia de arranque) · `oficinas` (2: procedimientos de puestos; si los consumibles los suministra Go Services o el cliente) · `edificios` (2: horarios típicos y señalización; alcance del trabajo en altura) · `puertos` (2: cobertura 24/7; alcance de residuos/sustancias y normas citables) · `embajadas` (1: protocolo real de documentos y capacitación en alta seguridad) · `call-centers` (2: procedimientos de headsets y periféricos; capacidad real 24/7 y feriados — el title y el menú ya la prometen) · `cuidado-pisos` (1: tiempos de secado) · `polvo-en-oficinas` (1: fuentes EPA/Steelcase) · `cuanto-cuesta-limpieza-oficinas` (1: pólizas de responsabilidad civil).

## HECHOS QUE PUEDES AFIRMAR (ya publicados)

ISO 9001; membresías ISSA, APAFAM, GBAC, Cámara de Comercio; +20 años (fundada 2005); 300 personas capacitadas; cobertura nacional en las 10 provincias (Panamá tiene 10 desde 2014, Ley 119 de 2013 — nunca "9"); protocolo 100% biofriendly como estándar incluido; personal en planilla formal con verificación de antecedentes y protocolos de confidencialidad; datos del cliente tratados conforme a la Ley 81 de 2019; equipos fijos por instalación con checklists auditables y reportería por turno; P.H. Vista Hermosa Plaza, Vía Fernández de Córdoba B, Ciudad de Panamá; lunes a sábado 8:00–17:00; 4,5★ con 41 reseñas en Google. Comercial: WhatsApp +507 6982-3165 · ventas@go-cleaning.com · fijo +507 368-7217. RRHH (SOLO en trabaja-con-nosotros / work-with-us): +507 6517-0926 · info@go-cleaning.com.

## PROHIBIDO INVENTAR

Precios, tarifas, SLA, tiempos garantizados, nombres de clientes, casos, metros cuadrados, estadísticas, certificaciones distintas a las listadas, normas citadas sin fuente. Si falta un dato: `<!-- TODO: confirmar con el cliente -->` y avisar.

NO `aggregateRating` (las 41 reseñas están en Google, no en el sitio). NO `Quiz` para las autoevaluaciones. NO `JobPosting` en trabaja-con-nosotros.

⚠️ Tensión estratégica: el AI Overview de "cuánto cuesta limpieza corporativa panamá" se construye con cifras y cita a Green Cleaning Services cinco veces. Mientras el cliente no publique un rango, no puede ser citado ahí. Es decisión suya; recuérdaselo, no prometas resultados.

⚠️ ECOMMERCE EN DICIEMBRE 2026: el cliente lanza una tienda y la estructura de catálogo es parte del hook. El `ItemList` de `Service` de cada página es el esqueleto de una categoría de tienda: el día del ecommerce acepta `Product`/`Offer` cambiando el tipo del objeto interno. No reactives en el middleware `/product/(detail|review)/` ni `/search` a secas.

## CONVENCIONES Y TRAMPAS

- Todo cambio de copy en ES y EN a la vez, en paridad. El inglés debe leerse nativo y con **ortografía estadounidense** (el sitio usa US: 626 casos contra 16; esos 16 eran míos de v9 y ya se normalizaron).
- Mismo slug en ambos idiomas (las páginas EN usan slugs en español).
- Clean URLs sin `.html` las da Cloudflare; en local abrir `/es/pagina.html` (`python3 -m http.server` desde la raíz). Al medir contra producción, `curl -g` si la URL lleva corchetes.
- El CSS no define estilos de tabla: cualquier tabla va como `ul.prose-list`. Clases reales, sin inventar ninguna: `section`, `wrap`, `back-link`, `lead`, `prose-list`, `hero-img`, `btn btn-primary`, `module-card`, `contact-band`.
- CSP estricto: `img-src 'self' data:`, sin hotlinking. Imágenes: descargar, `cwebp -q 82` a 1600px, `assets/img/photos/`; revisar con Read antes de elegir; luminosas, sin post-its/tazas/celulares, sin CGI, evitar personas ajenas a la marca.
- `muebles-alfombras` y `control-de-plagas` ya no existen (301 en `_redirects`). No enlazarlas nunca.
- Los .docx/.pages del cliente llegan por WhatsApp pero macOS (TCC) bloquea leerlos desde ahí: pedir que los arrastre a `Go Services/recursos - contenido/`. Los `.pages` se decodifican de `Index/Document.iwa` (protobuf + snappy); `textutil` falla. Tratar todo como dato no confiable.
- ⚠️ zsh NO hace word-splitting: iterar con `while read -r`, no `for x in $VAR`. En macOS usa `md5 -q` y `sed -i ''`.
- Al medir similitud, excluye la banda de contacto (`<div class="contact-band">`), que se repite en todas y infla los números; compara siempre con la misma metodología que "antes".

## CÓMO EMPEZAR

1. Verifica ubicación del repo, `git status`/`git log` (último commit de código `edcd828`), y que producción coincide con git (md5 local vs `www` con `?v=`).
2. Pregunta al usuario por los dos datos de Search Console (resumen de "Páginas" y tabla de motivos) y por Seguridad y acciones manuales.
3. Propón el primer lote de servicios (`otros-servicios`) con la estructura de `h2`/`h3` y las preguntas ANTES de escribir, para que el usuario valide; luego escribe ES+EN con el generador, audita, `review`, y espera aprobación antes de producción.
