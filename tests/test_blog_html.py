def test_blog_title_class_is_title(site):
    print(list(site.output_path.joinpath("blog").iterdir()))
    assert site.output_path.joinpath("blog", "test-blog-post.html").read_text().find('class="title"')
