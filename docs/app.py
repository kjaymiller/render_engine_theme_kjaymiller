from render_engine.site import Site
from render_engine.collection import Collection
from render_engine.page import Page


app = Site()

@app.collection
class Pages(Collection):
    content_path = 'pages'

@app.page
class Index(Page):
    template = 'index.html'
