from playwright.sync_api import sync_playwright
from render_engine import Site, Page, Collection, Blog
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


    test_blog_dir = tmp_path_factory.getbasetemp() / "blog"
    test_blog_dir.mkdir()
    test_blog_dir.joinpath("test_blog_post.md").write_text(
        "---\ntitle: Test Blog Post\ndate: 2023-10-29 12:00:00+04:00\n---\n\nThis is a test blog post"
    )

    @test_site.page
    class TestPage(Page):
        template='index.html'
        title="index"

    @test_site.collection
    class TestBlog(Blog):
        content_path = test_blog_dir
        routes = ["blog"]
        template = "blog.html"
    @test_site.collection
    class TestCollection(Collection):
        content_path = "tests"
        PageParser = MarkdownPageParser

    test_site.render()
    return test_site
    

@pytest.fixture(scope="session")
def live_server(site):
    _server = spawn_server(('localhost', 8000), site.output_path)

    p = Process(target=_server.serve_forever())
    p.start()
    yield
    p.kill()