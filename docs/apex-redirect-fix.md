# Arreglo del redirect del dominio sin www (go-cleaning.com)

**Para: Efrain** · servidor `144.126.158.220` (Apache)
**Verificado el 2026-10-15**

## El problema

El redirect del apex descarta la ruta. Devuelve siempre `Location: https://www.go-cleaning.com`
sin la parte de la URL que venía detrás, así que **todas** las páginas del dominio sin `www`
acaban en la portada en español:

```
$ curl -sI https://go-cleaning.com/es/servicios | grep -i location
Location: https://www.go-cleaning.com          <-- deberia ser .../es/servicios
```

Comprobado con tres rutas distintas; todas terminan en `https://www.go-cleaning.com/es/`.

## Por qué importa

- Cualquier enlace externo que apunte al dominio sin `www` hacia una página concreta
  manda al visitante a la portada, no a la página que pidió.
- Google interpreta ese 301 como "esta página concreta es la portada", de modo que la
  autoridad de esos enlaces no llega a la página que deberia recibirla.
- `go-cleaning.com/sitemap.xml` devuelve HTML en lugar del sitemap.
- Un visitante en inglés que llegue por una URL `/en/...` del apex aterriza en español.

El certificado del apex está correcto desde la renovación del 16 de septiembre
(vence el 15 de diciembre de 2026), eso no es parte del problema.

## El arreglo

En la configuración del VirtualHost del puerto 443 de `go-cleaning.com`, la directiva
debe conservar el resto de la URL. Con `Redirect` de mod_alias basta:

```apache
<VirtualHost *:443>
    ServerName go-cleaning.com

    # Conserva ruta y query: /es/servicios -> https://www.go-cleaning.com/es/servicios
    Redirect permanent / https://www.go-cleaning.com/
</VirtualHost>
```

Equivalente con mod_rewrite, si ya se usa ahí:

```apache
RewriteEngine On
RewriteCond %{HTTP_HOST} ^go-cleaning\.com$ [NC]
RewriteRule ^(.*)$ https://www.go-cleaning.com/$1 [R=301,L]
```

Lo que **no** funciona y es probablemente lo que hay ahora: una regla que apunta a
`https://www.go-cleaning.com` sin barra final ni `$1`, porque descarta la ruta.

Recargar después: `sudo systemctl reload apache2` (o `httpd`).

## Cómo comprobar que quedó bien

```bash
curl -sI https://go-cleaning.com/es/servicios | grep -i location
# esperado: Location: https://www.go-cleaning.com/es/servicios

curl -sIL https://go-cleaning.com/es/servicios -o /dev/null -w "%{num_redirects} saltos -> %{url_effective}\n"
# esperado: 1 saltos -> https://www.go-cleaning.com/es/servicios
```

## La alternativa que elimina el servidor

Este Apache existe solo para hacer un 301, y es un punto de fallo con mantenimiento
propio — ya dejó caducar el certificado una vez (11 de septiembre de 2026).

Moviendo los nameservers del dominio de Route 53 a Cloudflare, el apex resuelve
directamente a Cloudflare Pages por CNAME flattening, los certificados se emiten y
renuevan solos para apex y `www`, el 301 se configura con una Redirect Rule y este
servidor desaparece. Route 53 no puede hacerlo hoy porque su registro ALIAS solo
admite recursos de AWS.
