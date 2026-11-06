#!/usr/bin/env python3
"""Reescribe el par limpieza-hospitalaria (servicio) / hospitales (industria), ES y EN.

Contenido en estructuras Python; el HTML visible se renderiza desde ellas y el
schema (FAQPage + ItemList) se GENERA PARSEANDO ese HTML, nunca a mano, y se
verifica que cada pregunta y cada fragmento de respuesta aparece literal en el
texto visible.

Uso: python3 -I build_pair.py <repo>
"""
import html as H
import json
import re
import sys
from pathlib import Path

REPO = Path(sys.argv[1])
ORG = "https://www.go-cleaning.com/#organization"


# ---------------------------------------------------------------- render
def esc(t):
    return H.escape(t, quote=False)


def render(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f'      <p style="margin-top:12px">{val}</p>')
        elif kind == "p20":
            out.append(f'      <p style="margin-top:20px">{val}</p>')
        elif kind == "h2":
            out.append(f'\n      <h2 style="margin-top:40px">{esc(val)}</h2>')
        elif kind == "h3":
            out.append(f'\n      <h3 style="margin-top:28px">{esc(val)}</h3>')
        elif kind == "ul":
            lis = "\n".join(f"          <li>{li}</li>" for li in val)
            out.append(f'      <ul class="prose-list">\n{lis}\n      </ul>')
        elif kind == "todo":
            out.append(f"      <!-- TODO: {val} -->")
        else:
            raise ValueError(kind)
    return "\n".join(out)


# ---------------------------------------------------------------- parse
def strip_tags(s):
    s = re.sub(r"</?(a|strong|em|b|i|span)\b[^>]*>", "", s)  # en linea: sin espacio
    s = " ".join(H.unescape(re.sub(r"<[^>]+>", " ", s)).split())
    return re.sub(r"\s+([.,;:?!])", r"\1", s)


def parse_main(main_html):
    """Devuelve lista de ('h2'|'h3'|'p'|'li', texto) en orden de documento."""
    items = []
    for m in re.finditer(r"(?is)<(h2|h3|p|li)\b[^>]*>(.*?)</\1>", main_html):
        items.append((m.group(1).lower(), strip_tags(m.group(2))))
    return items


def is_q(t):
    return t.endswith("?") or ("¿" in t and "?" in t)


def build_faq(items, page_url, lang):
    faq, i = [], 0
    while i < len(items):
        k, t = items[i]
        if k == "h2" and is_q(t):
            j, parts = i + 1, []
            while j < len(items) and items[j][0] != "h2":
                if items[j][0] == "h3":
                    break  # la respuesta es solo la introduccion; las h3 son subcategorias
                parts.append(items[j][1])
                j += 1
            faq.append((t, parts))
        i += 1
    ents = []
    for q, parts in faq:
        ans = " ".join(p if p[-1] in ".?!:" else p + "." for p in parts)
        ents.append({"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": ans}})
    return faq, {"@context": "https://schema.org", "@type": "FAQPage",
                 "@id": f"{page_url}#faq", "mainEntity": ents}


def build_itemlist(items, page_url, list_id, list_name, service_type, lang):
    subs = [t for k, t in items if k == "h3" and not is_q(t)]
    area = "Panamá" if lang == "es" else "Panama"
    return subs, {
        "@context": "https://schema.org", "@type": "ItemList",
        "@id": f"{page_url}#{list_id}", "name": list_name,
        "numberOfItems": len(subs),
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "itemListElement": [
            {"@type": "ListItem", "position": n + 1,
             "item": {"@type": "Service", "name": s, "serviceType": service_type,
                      "provider": {"@id": ORG},
                      "areaServed": {"@type": "Country", "name": area}}}
            for n, s in enumerate(subs)],
    }


def ld(obj):
    return ('<script type="application/ld+json">'
            + json.dumps(obj, ensure_ascii=False) + "</script>")


# ---------------------------------------------------------------- aplicar
def apply(page):
    path = REPO / page["file"]
    s = path.read_text(encoding="utf-8")
    lang = page["lang"]
    url = page["url"]

    # 1) cuerpo: desde <h1 ...> hasta el boton CTA (incluido) dentro de la seccion
    m = re.search(r'(?s)(      <h1 style="margin-top:8px">).*?'
                  r'(\n    </div>\n  </section>)', s)
    assert m, page["file"]
    body = (
        f'      <h1 style="margin-top:8px">{esc(page["h1"])}</h1>\n'
        f'      <img class="hero-img" style="margin-top:24px;aspect-ratio:16/9" '
        f'src="/assets/img/photos/{page["img"]}" alt="{esc(page["alt"])}" />\n'
        f'      <p class="lead" style="margin-top:24px">{esc(page["lead"])}</p>\n\n'
        + render(page["blocks"]) + "\n\n"
        f'      <h2 style="margin-top:40px">{esc(page["cta_h2"])}</h2>\n'
        f'      <p style="margin-top:12px">{page["cta_p"]}</p>\n'
        f'      <a class="btn btn-primary" href="{page["cta_href"]}" '
        f'style="margin-top:32px">{esc(page["cta_btn"])}</a>'
    )
    s = s[:m.start()] + body + s[m.start(2):]

    # 2) meta descripcion (description, og, twitter)
    d = esc(page["meta"]).replace('"', "&quot;")
    s = re.sub(r'(<meta name="description" content=")[^"]*(")', rf"\g<1>{d}\2", s)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*(")', rf"\g<1>{d}\2", s)
    s = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', rf"\g<1>{d}\2", s)

    # 3) description del Service existente
    s = re.sub(r'("@type": "Service", "name": "[^"]*", "description": ")[^"]*(")',
               lambda mm: mm.group(1) + page["svc_desc"].replace('"', '\\"') + mm.group(2), s, count=1)

    # 4) schema generado desde el HTML ya escrito
    main = re.search(r"(?is)<main.*?</main>", s).group(0)
    items = parse_main(main)
    faq_src, faq = build_faq(items, url, lang)
    subs, il = build_itemlist(items, url, page["list_id"], page["list_name"],
                              page["service_type"], lang)

    # quita bloques previos de ItemList/FAQPage de esta pagina si se reaplica
    s = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", '
               r'"@type": "(?:ItemList|FAQPage)".*?</script>\n', "", s)
    bc = re.search(r'<script type="application/ld\+json">\{"@context": "https://schema.org", '
                   r'"@type": "BreadcrumbList".*?</script>\n', s)
    assert bc
    s = s[:bc.end()] + ld(il) + "\n" + ld(faq) + "\n" + s[bc.end():]

    # 5) verificacion: todo lo declarado esta en el texto visible
    visible = " ".join(t for _, t in items)
    vnorm = visible
    bad = []
    for q, parts in faq_src:
        if q not in vnorm:
            bad.append(("pregunta", q))
        for p in parts:
            if p not in vnorm:
                bad.append(("respuesta", p[:60]))
    for sname in subs:
        if sname not in vnorm:
            bad.append(("subcategoria", sname))
    for e in faq["mainEntity"]:
        for frag in re.split(r"(?<=[.?!:])\s+", e["acceptedAnswer"]["text"]):
            if frag and frag.rstrip(".") not in vnorm:
                bad.append(("fragmento", frag[:60]))
    assert not bad, (page["file"], bad)

    path.write_text(s, encoding="utf-8")
    words = sum(len(t.split()) for k, t in items)
    print(f'{page["file"]}: {words} palabras, {len(faq_src)} preguntas FAQ, {len(subs)} subcategorias ItemList')


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    import importlib
    PAGES = importlib.import_module(sys.argv[2]).PAGES
    for pg in PAGES:
        apply(pg)
