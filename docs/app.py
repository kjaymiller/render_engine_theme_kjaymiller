from render_engine.collection import Collection
from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser
from render_engine.site import Site

from render_engine_theme_kjaymiller import kjaymiller

app = Site()
app.site_vars.update ({
    "SITE_TITLE": "Kjaymiller Render Engine Theme",
    "SITE_AUTHOR": {
        "name": "kjaymiller",
        "email": "kjaymiller@gmail.com",
    },
    "theme": {}
})
app.register_themes(kjaymiller)

@app.collection
class Pages(Collection):
    content_path = 'docs/pages'
    template = "page.html"
    Parser = MarkdownPageParser
    

@app.page
class Index(Page):
    template = "page.html"
    title = ""
    slug = "index"
    Parser = MarkdownPageParser
    content_path = "README.md"
