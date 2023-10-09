from render_engine.collection import Collection
from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser
from render_engine.site import Site

from render_engine_theme_kjaymiller import kjaymiller

app = Site()
app.output_path = "docs/output"
app.site_vars.update ({
    "SITE_TITLE": "Kjaymiller Render Engine Theme",
    "SITE_URL": "https://kjaymiller.github.io/render_engine_theme_kjaymiller/",
    "SITE_AUTHOR": {
        "name": "kjaymiller",
        "email": "kjaymiller@gmail.com",
    },
    "NAVIGATION": [
        {
            "text": "Docs",
            "url": "/docs.html",
        },
        {
            "test": "GitHub",
            "url": "https://github.com/kjaymiller/render_engine_kjaymiller_theme",
            "icon": "fa-brands fa-github",
        }    
    ],
    "theme": {
        "title_size": "small",
        "colors": {
            "main": "indigo-200",
        },
        "social": {
            "github": "https://github.com/kjaymiller/render_engine_kjaymiller_theme",
            "x-twitter": "https://twitter.com/kjaymiller",
            "linkedin": "https://www.linkedin.com/in/kjaymiller/",
            "mastodon": "https://mastodon.social/@kjaymiller",
        },
        "fontawesome": "94d9a219ee"
    }
})
app.register_themes(kjaymiller)

@app.collection
class Docs(Collection):
    content_path = 'docs/pages'
    template = "page.html"
    Parser = MarkdownPageParser
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite", "header-ids"]}
    has_archive = True
    archive_template = "blog_list.html"

@app.page
class Index(Page):
    template = "page.html"
    title = ""
    slug = "index"
    Parser = MarkdownPageParser
    content_path = "README.md"
    parser_extras = {"markdown_extras": ["fenced-code-blocks", "codehilite"]}
