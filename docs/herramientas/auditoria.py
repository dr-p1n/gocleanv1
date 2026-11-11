# -*- coding: utf-8 -*-
"""Auditoria previa al deploy. Se corre sobre TODO el sitio, no solo lo tocado.

    python3 -I docs/herramientas/auditoria.py "$PWD" [pagina.html ...]

Las paginas que se pasen como argumento extra se revisan ademas contra la lista
de palabras sensibles (precios, garantias, certificaciones, porcentajes, 24/7),
que no fallan la auditoria pero se imprimen para revisarlas a ojo.

Linea base al cierre de v11: 270 bloques JSON-LD, 0 enlaces rotos, 0 fallas.
"""
import html as H
import json
import re
import sys
from pathlib import Path

REPO = Path(sys.argv[1])
fail = 0


def err(msg):
    global fail
    fail += 1
    print("  FALLA:", msg)


pages = sorted(list(REPO.glob("es/*.html")) + list(REPO.glob("en/*.html")))

# ---------------------------------------------------------- 1) JSON-LD
print("1) JSON-LD")
total = 0
for p in pages:
    s = p.read_text(encoding="utf-8")
    for m in re.finditer(r'(?s)<script type="application/ld\+json">(.*?)</script>', s):
        total += 1
        try:
            json.loads(m.group(1))
        except Exception as e:
            err(f"{p.relative_to(REPO)}: {e}")
print(f"  {total} bloques, todos parsean" if not fail else f"  {total} bloques")

# ---------------------------------------------------------- 2) enlaces internos
print("2) Enlaces internos")
checked = broken = 0
for p in pages:
    s = p.read_text(encoding="utf-8")
    for m in re.finditer(r'href="([^"#?][^"]*)"', s):
        h = m.group(1)
        if h.startswith(("http://", "https://", "mailto:", "tel:", "//")):
            continue
        checked += 1
        t = h.split("#")[0].split("?")[0]
        if not t:
            continue
        base = REPO if t.startswith("/") else p.parent
        q = (base / t.lstrip("/")).resolve()
        if q.exists() or Path(str(q) + ".html").exists():
            continue
        broken += 1
        err(f"{p.relative_to(REPO)} -> {h}")
print(f"  {checked} enlaces revisados, {broken} rotos")

# ---------------------------------------------------------- 3) paridad ES/EN
print("3) Paridad de estructura ES/EN")


def shape(path):
    s = path.read_text(encoding="utf-8")
    main = re.search(r"(?is)<main.*?</main>", s).group(0)
    body = re.search(r'(?s)<h1 style="margin-top:8px">.*?\n    </div>\n  </section>', main)
    chunk = body.group(0) if body else main
    return [m.group(1).lower() for m in re.finditer(r"(?is)<(h1|h2|h3|p|ul|li|a|img)\b", chunk)]


for p in sorted(REPO.glob("es/*.html")):
    q = REPO / "en" / p.name
    if not q.exists():
        continue
    a, b = shape(p), shape(q)
    if a != b:
        err(f"{p.name}: ES {len(a)} nodos vs EN {len(b)} (o distinto orden)")

# ------------------------------------------- 4) espacios antes de puntuacion
print("4) Espacios antes de puntuacion en el schema")
for p in pages:
    s = p.read_text(encoding="utf-8")
    for m in re.finditer(r'(?s)<script type="application/ld\+json">(.*?)</script>', s):
        o = json.loads(m.group(1))
        if isinstance(o, dict) and o.get("@type") == "FAQPage":
            for e in o["mainEntity"]:
                for t in (e["name"], e["acceptedAnswer"]["text"]):
                    if re.search(r"\s[.,;:?!]", t):
                        err(f"{p.relative_to(REPO)}: {t[:70]!r}")

# ------------------------------------------- 5) schema anclado al texto visible
print("5) Cada pregunta/respuesta/subcategoria aparece en el texto visible")


def visible(path):
    s = path.read_text(encoding="utf-8")
    main = re.search(r"(?is)<main.*?</main>", s).group(0)
    out = []
    for m in re.finditer(r"(?is)<(h2|h3|p|li)\b[^>]*>(.*?)</\1>", main):
        t = re.sub(r"</?(a|strong|em|b|i|span)\b[^>]*>", "", m.group(2))
        t = " ".join(H.unescape(re.sub(r"<[^>]+>", " ", t)).split())
        out.append(re.sub(r"\s+([.,;:?!])", r"\1", t))
    return " ".join(out)


for p in pages:
    s = p.read_text(encoding="utf-8")
    v = visible(p)
    for m in re.finditer(r'(?s)<script type="application/ld\+json">(.*?)</script>', s):
        o = json.loads(m.group(1))
        if not isinstance(o, dict):
            continue
        if o.get("@type") == "FAQPage":
            for e in o["mainEntity"]:
                if e["name"] not in v:
                    err(f"{p.relative_to(REPO)}: pregunta fuera del texto: {e['name'][:60]!r}")
                for frag in re.split(r"(?<=[.?!:])\s+", e["acceptedAnswer"]["text"]):
                    if frag and frag.rstrip(".") not in v:
                        err(f"{p.relative_to(REPO)}: respuesta fuera del texto: {frag[:60]!r}")
        if o.get("@type") == "ItemList":
            for it in o["itemListElement"]:
                if "item" not in it:
                    continue  # ItemList de navegacion (name+url), no de subcategorias
                if it["item"]["name"] not in v:
                    err(f"{p.relative_to(REPO)}: subcategoria fuera del texto: {it['item']['name']!r}")

# ---------------------------------------------------------- 6) palabras sensibles
print("6) Palabras sensibles en las paginas tocadas")
PAT = [r"\$", r"garantiz", r"certificad", r"\d\s?%", r"24/7", r"24 ?horas",
       r"guarantee", r"certified"]
for n in sys.argv[2:]:
    for lang in ("es", "en"):
        p = REPO / lang / n
        if not p.exists():
            continue
        v = visible(p)
        for pat in PAT:
            for m in re.finditer(pat, v, re.I):
                a = max(0, m.start() - 45)
                print(f"  REVISAR {lang}/{n}: ...{v[a:m.end() + 45]}...")

print()
print("FALLAS:", fail)
sys.exit(1 if fail else 0)
