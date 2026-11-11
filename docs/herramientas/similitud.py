# -*- coding: utf-8 -*-
"""Similitud de trigramas entre paginas ES, SIN la banda de contacto.

    python3 -I docs/herramientas/similitud.py "$PWD" pagina.html

La banda de contacto se repite en las 36 paginas e infla los numeros; excluirla
es lo que hace comparables las cifras de v10 en adelante. Referencia: tras las
reescrituras de v10/v11 ninguna pareja pasa de 5,4% (hospitales / colegios, que
comparten el marco de preguntas de industria y son el techo conocido).
"""
import html as H
import re
import sys
from pathlib import Path

REPO = Path(sys.argv[1])
TARGET = sys.argv[2]


def texto(path):
    s = path.read_text(encoding="utf-8")
    main = re.search(r"(?is)<main.*?</main>", s).group(0)
    main = re.sub(r'(?is)<div class="contact-band".*?</div>\s*</div>', " ", main)
    main = re.sub(r"(?is)<script.*?</script>", " ", main)
    t = " ".join(H.unescape(re.sub(r"<[^>]+>", " ", main)).split()).lower()
    return re.sub(r"[^a-záéíóúñü ]", " ", t)


def tri(t):
    w = t.split()
    return {tuple(w[i:i + 3]) for i in range(len(w) - 2)}


tris = {p.name: tri(texto(p)) for p in sorted(REPO.glob("es/*.html"))}
a = tris[TARGET]

res = sorted(((100 * len(a & b) / len(a | b), n)
              for n, b in tris.items() if n != TARGET and a and b), reverse=True)

print(f"{TARGET} contra las demas paginas ES (trigramas, sin contact-band):")
for v, n in res[:12]:
    print(f"  {v:5.1f}%  {n}")
