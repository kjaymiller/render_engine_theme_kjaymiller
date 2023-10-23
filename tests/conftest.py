from playwright.sync_api import sync_playwright
from render_engine import Site, Page, Collection
from render_engine.parsers.markdown import MarkdownPageParser
import render_engine_theme_kjaymiller.kjaymiller as theme
from render_engine.watcher.event import spawn_server
import http.server
import pytest
from multiprocessing import Process

@pytest.fixture(scope="session")
def site(tmp_path_factory):
    test_site = Site()
    test_site.site_vars.update ({"theme": {}})
    test_site.output_path = tmp_path_factory.getbasetemp() / "output"
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

    test_site.render()
    return test_site
    

@pytest.fixture(scope="session")
def live_server(site):
    _server = spawn_server(('localhost', 8000), site.output_path)

    p = Process(target=_server.serve_forever())
    p.start()
    yield
    p.kill()
