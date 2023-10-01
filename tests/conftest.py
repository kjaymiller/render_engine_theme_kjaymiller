from playwright.sync_api import sync_playwright
from render_engine import Site, Page, Collection
from render_engine.parsers.markdown import MarkdownPageParser
import render_engine_theme_kjaymiller.kjaymiller as theme
import http.server
import pytest
from multiprocessing import Process

@pytest.fixture(scope="session")
def site():
    test_site = Site()
    test_site.site_vars.update ({"theme": {}})
    test_site.output_path = 'tests/output'
    test_site.register_themes(theme)

    @test_site.page
    class TestPage(Page):
        template='index.html'
        title="index"

    @test_site.collection
    class TestCollection(Collection):
        content_path = "tests"
        PageParser = MarkdownPageParser
        template = "page.html" 

    return test_site.render()
    
def runserver():
    class server(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory="output", **kwargs)

    httpd = http.server.HTTPServer(('localhost', 8000), server)
    httpd.serve_forever()


@pytest.fixture(scope="session", autouse=True)
def live_server(site):
    site
    p = Process(target=runserver)
    p.start()
    yield
    p.kill()
