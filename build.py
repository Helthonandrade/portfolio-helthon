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
doc = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n' + head.strip() + "\n"
       '<meta property="og:title" content="Helthon Andráde · Potência">\n'
       '<meta property="og:description" content="Planner criativo, produtor executivo sênior e fundador da BAITA.">\n'
       '<meta property="og:image" content="https://portfolio.baita.site/assets/jobs/arcelor-out-RSbKWPf.jpg">\n'
       + style + "\n</head>\n<body>\n" + rest.strip() + "\n</body>\n</html>\n")
(dist / "index.html").write_text(doc, encoding="utf-8")
print("dist/index.html ok")
