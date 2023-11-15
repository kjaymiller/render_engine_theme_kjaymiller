import logging

import pytest
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import sync_playwright

axe = Axe()


@pytest.mark.skip(reason="This test is not working")
def test_index() -> None:
    """Run Axe on a URL and save the results to a file."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/")
        results = axe.run(page)
        print(page.inner_html("main"))
        page.close()
    if results.violations_count:
        logging.error(results.generate_report())
    assert results.violations_count <= 3
