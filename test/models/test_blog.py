import pytest


@pytest.mark.django_db
def test_blogger(blog):
    assert blog.title == "blog title0"
    assert blog.content == "blog content0"
