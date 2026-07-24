# Go Services — Sitio web · Documento de handoff (técnico)

**Sitio:** https://www.go-cleaning.com
**Repo:** este directorio (`gocleanv1`)
**Hosting:** Cloudflare Pages · proyecto `gocleanv1`
**Última actualización de este documento:** 2026-07-23

> Este archivo **no se publica** (está excluido en `deploy.sh`). Es solo para quien
> mantenga el sitio.

---

## 1. Qué es el sitio

Sitio estático (HTML/CSS/JS puro, sin framework ni build). Bilingüe: `/es/` y `/en/`,
66 páginas. URLs limpias sin `.html`.

Estructura:
- `es/`, `en/` — todas las páginas por idioma.
- `assets/css/style.css` — estilos (un solo archivo).
- `assets/js/calculators.js` — scorecards, cookie banner, lógica de lead capture.
- `assets/img/` — logo, favicons, og-image, certificaciones (`certs/`) y **fotos** (`photos/`).
- `_headers` — cabeceras HTTP (seguridad + indexación + caché) de Cloudflare Pages.
- `_redirects` — reglas de redirección de Pages.
- `sitemap.xml`, `robots.txt` — SEO.
- `google7c0bb552082a0bfe.html` — verificación de Google Search Console (**no borrar**).
- `apps-script/` — código del backend de lead capture (Google Apps Script). **No se publica.**
- `deploy.sh` — script de despliegue. **No se publica.**

---

## 2. Cómo desplegar

**Usar SIEMPRE el script, nunca `wrangler pages deploy` directo.**

```bash
./deploy.sh review   # preview para el cliente -> https://review.gocleanv1.pages.dev
./deploy.sh main     # PRODUCCIÓN            -> https://www.go-cleaning.com
```

**Por qué el script:** `wrangler pages deploy .` sube *todo* el directorio salvo una lista
fija (node_modules, .git, .DS_Store, functions, _worker.js, .wrangler) y **no** lee
`.assetsignore`. Deployar la raíz publicaría `apps-script/`, `README.md`, `HANDOFF.md`, etc.
`deploy.sh` hace `rsync` a una copia limpia (excluye `.git`, `.claude`, `apps-script`,
`README.md`, `deploy.sh`, `HANDOFF.md`, `docs/`, `.DS_Store`) y sube esa copia.

**Verificar en vivo:** el CDN de `www` tiene lag de propagación. Para confirmar al instante,
usar la URL fresca que imprime el deploy (`<hash>.gocleanv1.pages.dev`) o `curl` con
cache-buster:

```bash
curl -s "https://www.go-cleaning.com/es/?v=$(date +%s)" | grep '<title>'
```

---

## 3. Dominio y DNS  (⚠️ leer antes de tocar nada)

- **`www.go-cleaning.com` es el dominio canónico.** Todo el sitio (canonical, og:url,
  hreflang, sitemap, robots) apunta a `https://www.go-cleaning.com`.
- DNS del dominio vive en **AWS Route 53** (lo maneja **Efrain**, IT del cliente), no en Cloudflare.
- `www` → CNAME → `gocleanv1.pages.dev` (así llega a Cloudflare Pages).
- **El apex `go-cleaning.com` NO puede apuntar a Pages.** Cloudflare Pages no soporta dominio
  apex con DNS externo (requeriría que el apex fuera zona en Cloudflare). Route 53 no hace
  CNAME/ALIAS a un host externo. **No volver a intentar apuntar el apex a Pages.**
- El apex tiene un `A record` → `144.126.158.220` (servidor Apache viejo) con un **301 →
  `https://www.go-cleaning.com`** que puso Efrain. Funciona en HTTP y HTTPS.
  - Detalle conocido: ese 301 **no conserva la ruta** (todo cae en la home). Fue a propósito
    (las URLs viejas de WordPress no coinciden con las nuevas). Si algún día se quiere conservar
    la ruta, cambiar la regla por: `RewriteRule ^(.*)$ https://www.go-cleaning.com/$1 [R=301,L]`.
- **Email:** MX / SPF / DMARC del correo viven en Route 53. **NO TOCAR.**
- **HSTS** en `_headers` está deliberadamente **sin** `includeSubDomains` ni `preload`, para no
  forzar HTTPS sobre hosts de correo. No añadir esos flags sin auditar cada subdominio.

---

## 4. `_headers` y `_redirects`

- **`_headers`** — Cloudflare Pages. Incluye:
  - **CSP** (solo scripts propios, Google Fonts, imágenes self-hosted, y fetch al endpoint de
    Apps Script). Tras auto-hospedar las fotos, `img-src` ya **no** incluye Unsplash.
  - HSTS (1 año, sin includeSubDomains/preload), X-Frame DENY, nosniff, Referrer-Policy,
    Permissions-Policy, COOP.
  - `X-Robots-Tag: index, follow, max-image-preview:large, ...` (espeja el `<meta robots>`).
  - Caché: HTML `max-age=0, must-revalidate` (se revalida siempre por el lag del CDN);
    `/assets/*` `max-age=3600, stale-while-revalidate=86400`.
  - Resultado: **Mozilla Observatory A+**.
- **`_redirects`** — tiene dos reglas:
  1. `/google7c0bb552082a0bfe.html /google7c0bb552082a0bfe 200` — sirve el archivo de
     verificación de GSC en su URL exacta con 200 (Pages hace 308 de `.html` a la URL limpia,
     lo que rompía la verificación). **No borrar** esta regla ni el archivo.
  2. `/ /es/ 302` — la raíz redirige a español.

---

## 5. Imágenes (self-hosted)

Las fotos están en `assets/img/photos/*.webp` (22 archivos, WebP q82 ~1600px). Antes eran
hotlinks a `images.unsplash.com`; se auto-hospedaron para eliminar la dependencia externa,
mejorar LCP y poder quitar Unsplash del CSP.

- El mapa de qué archivo salió de qué foto original de Unsplash está en
  `docs/imagenes-unsplash-origen.txt`.
- Son fotos de Unsplash (licencia comercial sin atribución requerida). **Pendiente del cliente:**
  reemplazarlas por fotos propias/licenciadas cuando las tenga — basta con sobrescribir el
  `.webp` correspondiente en `assets/img/photos/` conservando el nombre, o actualizar el `src`
  en las páginas.

---

## 6. Lead capture (scorecards)

Dos scorecards (risk-audit y eco-audit) capturan a la **misma** Google Sheet ("Go Services -
Leads", en la cuenta del cliente).

- **Frontend:** `assets/js/calculators.js`. Config al inicio del archivo:
  `GAS_ENDPOINT` (URL `/exec` del Web App) y `GAS_TOKEN` (secreto compartido, debe coincidir
  con `SHARED_TOKEN` en Code.gs). El `GAS_TOKEN` es visible en el JS público — **no es un
  secreto real**, solo frena spam casual; no hay nada que rotar.
- **Backend:** `apps-script/Code.gs`, desplegado como **Web app** (Execute as: *Me*, Who has
  access: *Anyone*). Añade una fila por lead; columna **Source** distingue `risk-audit` vs
  `eco-audit`. `NOTIFY_EMAIL = hello@go-cleaning.com` recibe aviso por cada lead.
- **Flujo:** responder preguntas → **gate** con formulario (nombre/email/WhatsApp/empresa
  obligatorios) → manda el lead + descarga un reporte HTML branded → recién ahí revela
  resultados.
- **Redesplegar Code.gs tras editarlo:** en el editor de Apps Script → *Deploy → Manage
  deployments → (lápiz) → Version: New version → Deploy*. Si se crea un *deployment nuevo*
  cambia la URL `/exec` y hay que actualizar `GAS_ENDPOINT` en `calculators.js`.

---

## 7. Contacto público (en el sitio)

- WhatsApp: `https://wa.me/50769823165` (+507 6982-3165)
- Email público: `dabin.rivera@go-cleaning.com`
- No hay página de contacto: el contacto vive en el footer + los scorecards.

---

## 8. Accesos a transferir al cliente

| Recurso | Qué es | Responsable actual | A transferir a |
|---|---|---|---|
| Cloudflare Pages (proyecto `gocleanv1`) | Hosting del sitio + deploy | (equipo web) | cliente / quien mantenga |
| Google Search Console | Propiedad `https://www.go-cleaning.com` (verificada por archivo HTML) | (equipo web) | cliente |
| Google Sheet "Go Services - Leads" | Destino de los leads | cuenta del cliente | (ya del cliente) |
| Google Apps Script (Code.gs) | Backend de lead capture | cuenta del cliente | (ya del cliente) |
| DNS (Route 53) | Zona `go-cleaning.com` | Efrain (IT cliente) | (permanece con Efrain) |
| Repo git | Código fuente | (equipo web) | cliente / quien mantenga |

---

## 9. Pendientes del lado del cliente

1. **Confirmar el año de fundación.** El sitio publica `foundingDate: 2005` y "+20 años" en
   títulos, pero **no está verificado con el cliente**. Investigación externa (2026-07):
   LinkedIn y ZoomInfo dicen fundada/operando **desde 2007** (~19 años); un directorio (EL DEPH,
   con texto de la propia empresa) dice "más de 15 años". **Ninguna fuente externa respalda 2005.**
   Si el año correcto implica <20 años, hay que ajustar los títulos "+20 años" además del
   `foundingDate` en los 112 bloques JSON-LD (66 páginas).
2. **Revisión legal de la Política de Privacidad** (`/es/privacidad`, `/en/privacy`) contra la
   Ley 81 de 2019 — pendiente, requiere abogado.
3. **Reemplazar las fotos** de Unsplash por fotos propias/licenciadas (ver §5).
4. **Google Search Console:** enviar `sitemap.xml` y solicitar indexación de las páginas
   prioritarias (ver `docs/GSC-y-Sheet-checklist.md`).
5. **Borrar la fila de prueba** `TEST — BORRAR` (source: test-curl) de la Google Sheet si sigue.
6. **Definir la mantención:** a quién queda el sitio y el traspaso de accesos (§8).
