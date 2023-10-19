import pytest


@pytest.mark.django_db
def test_comment(comment, blog, blogger):
    assert comment.blog == blog
    assert comment.blogger == blogger
    assert comment.comment == "comment0"
