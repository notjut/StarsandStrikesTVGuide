"""Build index.html for GitHub Pages: python3 build/build.py  (run data.py first, or let this run it)."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(HERE, "data.py")], check=True)
tpl = open(os.path.join(HERE, "template.html")).read()
data = open(os.path.join(HERE, "data.json")).read().replace("</", "<\\/")
logo = open(os.path.join(HERE, "logo.b64")).read()
page = tpl.replace("__DATA__", data).replace("__LOGO__", logo)
head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>html{color-scheme:light dark}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n')
# move <title> and <meta>/<link>/<style> block into <head>; everything else into <body>
cut = page.index("</style>") + len("</style>")
html = head + page[:cut] + "\n</head>\n<body>" + page[cut:] + "\n</body>\n</html>\n"
open(os.path.join(HERE, "..", "index.html"), "w").write(html)
print("wrote index.html", len(html), "bytes")
