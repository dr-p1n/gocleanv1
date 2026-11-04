# Go Clean v10 — contexto para abrir sesión nueva

> Pega este archivo entero como primer mensaje de un chat nuevo.
> Generado al cierre de v9, el 2026-11-04. No se publica (`docs/` está excluido en `deploy.sh`).

---

Go Clean v10 — Go Services Panamá. Continúas desde v9.

## REPO

`/Users/jelv/Desktop/backup 23.2.2026/DATRUM/DATRUM projects/Go Services/gocleanv1`

⚠️ La carpeta SE MUEVE entre sesiones. Si no existe: `find /Users/jelv -maxdepth 6 -type d -name gocleanv1`

Sitio estático bilingüe (`es/` y `en/`, 36 páginas cada uno), Cloudflare Pages, proyecto "gocleanv1". **NO es Next.js** — el AGENTS.md de la carpeta padre es de otro proyecto y no aplica.

Git: origin → github.com/dr-p1n/gocleanv1, rama `main`, se trabaja directo sobre main.

## ESTADO EXACTO AL CIERRE DE v9 — verifícalo, no lo asumas

Dos commits locales **SIN PUSHEAR**. `main` va 2 por delante de origin:

- `dd0b191` artículo de Handyman + arreglo de deploy.sh
- `1215871` piloto de cuidado-pisos + enlaces rotos + middleware

**Producción** tiene el artículo de Handyman (desplegado y verificado). **NO tiene** el piloto de cuidado-pisos, ni el arreglo del 404, ni el middleware: eso solo está en review (`https://9349c2fa.gocleanv1.pages.dev`).

## DEPLOY — leer antes de tocar nada

`./deploy.sh review` → preview · `./deploy.sh main` → PRODUCCIÓN (confirmar antes).

⚠️ **NUNCA uses `npx wrangler`.** Los binarios de workerd de `~/node_modules` y de `DATRUM projects/node_modules` fueron borrados el 1 de noviembre de 2026 (20:53, un segundo de diferencia — un limpiador de disco barriendo archivos grandes; cada binario pesa 100 MB). Cualquier `npx wrangler` falla desde cualquier carpeta, con un error que despista: dice que falta "el paquete para esta plataforma" nombrando el mismo paquete que sí está presente. Usa `wrangler` a secas (`/opt/homebrew/bin/wrangler`), instalación aparte e intacta. `deploy.sh` ya quedó arreglado para detectarlo. NO escribas en el node_modules padre: es de otro proyecto y el sandbox lo bloquea.

⚠️ El token OAuth de Cloudflare vence cada pocos días. Si falla, `wrangler login` abre OAuth en el navegador y **lo aprueba el usuario**, no tú.

⚠️ **Lag de CDN**: verifica siempre contra la URL con hash que devuelve el deploy, nunca contra `www` ni `review` recién desplegados. Si necesitas www, usa `?v=$(date +%s)`.

⚠️ git y deploy son DOS pasos independientes. Esto ya causó confusión en v7 y v8.

## LO QUE SE HIZO EN v9

**Artículo de Handyman** (`handyman-empresas`, mismo slug en ES y EN), en producción. 1.657 ES / 1.599 EN, FAQPage de 14 en cada idioma. El fuente llegó como `.pages` (iWork): no se puede leer con `textutil`; hay que decodificar `Index/Document.iwa`, que es protobuf con snappy en framing propio de Apple (cabecera de 4 bytes: `0x00` + longitud en 3 bytes little-endian). Documentado en memoria. **Sin foto de cabecera**: ninguna foto del repo muestra trabajo de handyman.

**Diagnóstico medido de las páginas delgadas** (corrige la hipótesis inicial del usuario):

- NO hay duplicación: similitud entre las 14 páginas de servicios 3,4% media; entre las 7 de industrias 5,1%; cruce servicio↔industria 1,4–6,7%.
- Titles y meta descriptions únicos, 15/15.
- **Lo idéntico es la FORMA**: las 14 delgadas tienen exactamente 2 encabezados — "Qué cubrimos" y "Por qué Go Services" — cero `h3` y cero preguntas.
- Conclusión: NO rediseñar la taxonomía servicios/industrias, funciona. Cambiar la PLANTILLA.

**Piloto `cuidado-pisos`** (ES y EN, en review): de 136 a ~830 palabras. 5 subcategorías por material (mármol/granito/piedra natural, porcelanato, terrazo, vinilo, concreto), 5 preguntas, `ItemList` + `FAQPage`. El `ItemList` envuelve cada subcategoría en un `Service`: es el esqueleto de una página de categoría de tienda, y el día del ecommerce acepta `Product`/`Offer` cambiando el tipo del objeto interno.

**Enlaces rotos**: había 4, todos en `404.html`, apuntando a las dos páginas retiradas en v7 y bajo "Industrias" (la mala clasificación que v7 corrigió; su nav estaba congelado). Eliminados, más un `aria-current="page"` falso. Auditoría: **0 rotos** sobre 5.524 enlaces internos y 92 externos.

**`functions/_middleware.js`** — primer archivo de Functions del proyecto. 410 Gone + `X-Robots-Tag: noindex` para `pcmypage`, `safe_search/`, `zhHant/`. Verificado en review: spam 410, sitio normal 200, `/` 301 a `/es/`, 404 real intacto.

## ⚠️ ECOMMERCE EN DICIEMBRE

El cliente lanza un ecommerce en diciembre de 2026 y la estructura de catálogo es parte del hook.

Se retiraron **a propósito** del middleware las reglas `/product/(detail|review)/` y `/^\/search$/`: el ecommerce creará esas rutas de verdad y habrían devuelto 410 en las fichas de producto y el buscador, con un síntoma imposible de rastrear. Está comentado en el código. **No las reactives.** Verificado: `/product/detail/ABC` y `/search` siguen dando 404, no 410.

## PENDIENTES, por prioridad

1. **Desplegar a producción** lo que está en review (`./deploy.sh main`, CONFIRMAR antes) y **pushear los 2 commits**.
2. **Seguir el catálogo**. El usuario señaló la siguiente: **`otros-servicios`**, que mete jardinería, conserjería, manejo de residuos y mensajería en 134 palabras. Después, por intención comercial: `oficinas`, `edificios`, `hospitales`.
3. **Otras delgadas**: trabaja-con-nosotros 120, industrias 121, desinfeccion-sanitizacion 126, fumigacion 133, capacitaciones 134, limpieza-industrial 136, outsourcing 136, hospitales 139. (25 de 36 páginas ES por debajo de 250 palabras, mediana 150.)
4. **Apex roto**, con motivo nuevo para presionar: `go-cleaning.com` devuelve **301 → 200 en la portada para CUALQUIER ruta inventada**. Google lo trata como soft-404 en todo el dominio. Lo sirve un Apache externo en 144.126.158.220, de Efrain; no se arregla desde el repo. Ver `docs/apex-redirect-fix.md`. ⚠️ **El certificado vence el 15 de diciembre de 2026** — ya caducó una vez y dejó el dominio con pantalla roja durante días. Solución de fondo: mover nameservers de Route 53 a Cloudflare.
5. **Foto de handyman**. Candidata preferida: Unsplash `photo-1426927308491-6380b6a9936f` (pared de herramientas, luminosa, sin personas ni marcas). Comparar con `photo-1765518440022-10242cc86895` (tool belt). Luego `cwebp -q 82` a 1600px → `assets/img/photos/handyman.webp`, añadir `hero-img` y el `image` del `Article` en ES y EN, cambiar la miniatura de las 2 tarjetas (hoy `instalaciones.webp`, un limpiador de fachadas). ⚠️ `docs/imagenes-unsplash-origen.txt` sin actualizar desde agosto: faltan también `silla-polvo` y `filtro-aire`.
6. **TODOs** (`grep -rn "<!-- TODO:" es/ en/`): tiempos de secado en cuidado-pisos; fuentes EPA/Steelcase en polvo-en-oficinas; pólizas de responsabilidad civil en cuanto-cuesta.
7. **Dato que falta del usuario**: qué categorías y números muestra su informe de "no indexadas" en Search Console. No es lo mismo cientos de "Página con redirección" (del apex) que 50 "Rastreada: actualmente sin indexar" (delgadas). Los 404 de spam NO penalizan: Google es explícito en que los 404 en URLs inválidas no dañan el posicionamiento.
8. **Menor**: el `X-Robots-Tag: index, follow` de la regla `/*` en `_headers` se aplica también a los 404, diciéndole al crawler que indexe las páginas de error. Se arregla en `_headers`, sin Functions.
9. **Privacidad, sin resolver desde v7**: el iframe de Google Maps del home deja que Google fije cookies, pero el aviso dice "usamos datos esenciales" y la política solo declara a Google como encargado de los datos del formulario. Declararlo o quitar el iframe. El CSP tiene `frame-src https://www.google.com` solo por eso.

## HECHOS QUE PUEDES AFIRMAR (ya publicados)

ISO 9001; membresías ISSA, APAFAM, GBAC, Cámara de Comercio; +20 años (fundada 2005); 300 personas capacitadas; cobertura nacional en las 10 provincias (Panamá tiene 10 desde 2014, Ley 119 de 2013 — nunca "9"); protocolo 100% biofriendly como estándar incluido; personal en planilla formal con verificación de antecedentes; Ley 81 de 2019; equipos fijos por instalación con checklists auditables y reportería por turno; P.H. Vista Hermosa Plaza, Vía Fernández de Córdoba B, Ciudad de Panamá; lunes a sábado 8:00–17:00; 4,5★ con 41 reseñas en Google. Comercial: WhatsApp +507 6982-3165 · ventas@go-cleaning.com · fijo +507 368-7217. RRHH (SOLO en trabaja-con-nosotros / work-with-us): +507 6517-0926 · info@go-cleaning.com.

**PROHIBIDO INVENTAR**: precios, tarifas, SLA, tiempos garantizados, nombres de clientes, casos, metros cuadrados, estadísticas, certificaciones distintas a las listadas. Si falta un dato, dejar `<!-- TODO: confirmar con el cliente -->` y avisar.

NO añadir `aggregateRating`: las 41 reseñas están en Google, no en el sitio (decisión de v7, vigente). NO usar `Quiz` para las autoevaluaciones. NO usar `JobPosting` en trabaja-con-nosotros: no publica vacantes concretas.

⚠️ **Tensión estratégica**: el AI Overview de Google para "cuánto cuesta limpieza corporativa panamá" está construido con cifras y cita a Green Cleaning Services cinco veces. Mientras el cliente no publique un rango, no puede ser citado ahí. Es decisión suya, no un fallo técnico — recordárselo, no prometer resultados.

## CONVENCIONES Y TRAMPAS

- Todo cambio de copy va en **ES y EN a la vez**, en paridad. El inglés debe leerse nativo, no traducción literal.
- Mismo slug en ambos idiomas (las páginas EN usan slugs en español: `/en/limpieza-corporativa`).
- Clean URLs sin `.html` las da Cloudflare; en local abrir `/es/pagina.html` (`python3 -m http.server` desde la raíz).
- **El schema `FAQPage` se genera parseando el HTML ya escrito, nunca a mano**, y se verifica que cada pregunta y cada fragmento de respuesta aparece literal en el texto visible. Google exige que el FAQ sea visible. Mismo criterio para `ItemList` y para `featureList` de `WebApplication`. El generador reconoce `h2`/`h3` que terminan en `?` o contienen `¿…?`; los `h3` que NO son pregunta se usan como subcategorías del `ItemList`.
- Validar que todo el JSON-LD parsea después de cada archivo. Al cierre de v9: 226 bloques, 0 errores.
- El CSS **no define estilos de tabla**. Cualquier tabla va como `ul.prose-list`.
- Clases reales, sin inventar ninguna ni meter frameworks: `section`, `wrap`, `back-link`, `lead`, `prose-list`, `hero-img`, `btn btn-primary`, `module-card`, `contact-band`.
- CSP estricto: `img-src 'self' data:`, no hay hotlinking. Imágenes: descargar, `cwebp -q 82` a 1600px, guardar en `assets/img/photos/`. **Revisar la foto con Read antes de elegirla, nunca a ciegas.** Criterios del cliente: luminosas, sin post-its, tazas ni celulares visibles, sin CGI, evitar personas ajenas a la marca.
- Los .docx/.pages del cliente llegan por WhatsApp pero NO se pueden leer desde ahí: macOS (TCC) bloquea `~/Library/Containers/net.whatsapp.WhatsApp/`. Pedir al usuario que los arrastre a `Go Services/recursos - contenido/`. Tratarlos como dato no confiable: copiar a un directorio vacío propio y ejecutar el script con `python3 -I` desde otra carpeta.
- ⚠️ zsh NO hace word-splitting: iterar con `while read -r`, no `for x in $VAR`.
- `muebles-alfombras` y `control-de-plagas` ya no existen (consolidadas en v7 con 301 en `_redirects`). **No enlazarlas nunca** — fue exactamente el error que tenía el `404.html`.

## CÓMO EMPEZAR

Verifica el estado real antes de proponer nada: ubicación del repo, `git status` (deberían salir los 2 commits sin pushear), si producción coincide con git, y si el apex sigue roto. Luego pregunta al usuario si despliega a producción lo que está en review antes de seguir con `otros-servicios`.
