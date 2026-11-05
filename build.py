import re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"

app = (SRC / "app.html").read_text()
version = re.search(r'const VERSION = "([^"]+)"', app).group(1)

title_end = app.index("</title>") + len("</title>")
style_end = app.index("</style>") + len("</style>")

head_extra = """
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Eigen.wear">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>"""

register = (
    '<script>if("serviceWorker" in navigator&&location.protocol==="https:"){'
    'const had=!!navigator.serviceWorker.controller;let reloaded=false;'
    'navigator.serviceWorker.addEventListener("controllerchange",()=>{if(!had||reloaded)return;reloaded=true;location.reload();});'
    'addEventListener("load",()=>{navigator.serviceWorker.register("sw.js").then(r=>r.update()).catch(()=>{});});}</script>'
)

html = (
    '<!doctype html>\n<html lang="en">\n<head>\n'
    f"{app[:title_end]}{head_extra}{app[title_end:style_end]}\n</head>\n"
    f"<body>{app[style_end:]}\n{register}\n</body>\n</html>\n"
)

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()
(DIST / "index.html").write_text(html)
(DIST / "sw.js").write_text((SRC / "sw.js").read_text().replace("__VERSION__", version))
for name in ("manifest.webmanifest", "_headers"):
    shutil.copy(SRC / name, DIST / name)
for icon in (SRC / "icons").iterdir():
    shutil.copy(icon, DIST / icon.name)

print(f"Built Eigen.wear {version} -> {DIST}", file=sys.stderr)
