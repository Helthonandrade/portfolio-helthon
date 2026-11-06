"""Gera dist/ para o Render: envolve o index.html (fragmento usado no Claude Artifact) num documento HTML completo."""
import shutil, pathlib
root = pathlib.Path(__file__).parent
dist = root / "dist"
shutil.rmtree(dist, ignore_errors=True)
shutil.copytree(root / "assets", dist / "assets")
src = (root / "index.html").read_text(encoding="utf-8")
cut = src.index("<style>")
head, body = src[:cut], src[cut:]
style_end = body.index("</style>") + len("</style>")
style, rest = body[:style_end], body[style_end:]
URL = "https://portfolio.baita.site/"
IMG = URL + "assets/og-portfolio.jpg"
TITLE = "Helthon Andráde · Eu faço marca virar lugar"
DESC = "Planner criativo, produtor executivo sênior e fundador da BAITA. Assista ao reel e escolha um desafio: 4 poderes, 19 cases."
OG = "".join(f'<meta {k}="{n}" content="{v}">\n' for k, n, v in [
    ("property", "og:type", "website"), ("property", "og:site_name", "BAITA"), ("property", "og:locale", "pt_BR"),
    ("property", "og:url", URL), ("property", "og:title", TITLE), ("property", "og:description", DESC),
    ("property", "og:image", IMG), ("property", "og:image:secure_url", IMG), ("property", "og:image:type", "image/jpeg"),
    ("property", "og:image:width", "1200"), ("property", "og:image:height", "630"),
    ("property", "og:image:alt", "Plateia lotada diante de um palco iluminado, com o texto: Eu faço marca virar lugar. Assista ao reel."),
    ("name", "twitter:card", "summary_large_image"), ("name", "twitter:title", TITLE),
    ("name", "twitter:description", DESC), ("name", "twitter:image", IMG),
]) + f'<link rel="canonical" href="{URL}">\n'
doc = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n' + head.strip() + "\n"
       + OG
       + style + "\n</head>\n<body>\n" + rest.strip() + "\n</body>\n</html>\n")
(dist / "index.html").write_text(doc, encoding="utf-8")
print("dist/index.html ok")
