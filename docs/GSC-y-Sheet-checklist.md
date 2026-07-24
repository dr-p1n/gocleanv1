# Checklist — Google Search Console + Google Sheet

> Estas acciones se hacen en **cuentas del cliente** (GSC y la Google Sheet). Las ejecuta el
> cliente o quien tenga el login; no forman parte del deploy del sitio.

## A. Google Search Console

Propiedad: `https://www.go-cleaning.com` (prefijo de URL, ya **verificada** por archivo HTML).

1. **Enviar el sitemap**
   - GSC → *Sitemaps* (menú izquierdo).
   - En "Agregar un sitemap nuevo" escribir: `sitemap.xml`
   - *Enviar*. Debe quedar en estado "Correcto" (66 URLs).

2. **Solicitar indexación de las páginas prioritarias**
   Para cada URL: pegar en la barra *"Inspeccionar cualquier URL"* (arriba) → esperar el
   análisis → *Solicitar indexación*.
   - `https://www.go-cleaning.com/es/`
   - `https://www.go-cleaning.com/en/`
   - `https://www.go-cleaning.com/es/servicios`
   - `https://www.go-cleaning.com/es/bioseguridad`

3. **Revisar cobertura a los 2–3 días**
   - GSC → *Páginas* (Indexación) → confirmar que las páginas se van indexando y que no hay
     errores de cobertura.

## B. Google Sheet "Go Services - Leads"

1. Abrir la hoja (cuenta del cliente).
2. Buscar la fila de prueba con **Source = `test-curl`** y/o el texto **`TEST — BORRAR`**.
3. Borrar esa fila (clic derecho en el número de fila → *Eliminar fila*).
4. Confirmar que las cabeceras (fila 1) y los leads reales quedan intactos.
