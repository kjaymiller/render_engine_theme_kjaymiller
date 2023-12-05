def test_stylesheets_are_added(site):
    """asserts that tailwind and pygments stylesheets are added to the head"""
    output = site.output_path.joinpath("index.html").read_text()
    assert "static/css/tailwind.css" in output
    assert "static/css/pygments.css" in output
