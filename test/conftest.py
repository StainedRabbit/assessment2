import pytest
from factories import BloggerFactory, BlogFactory, CommentFactory


from pytest_factoryboy import register

from blogs.models import Blogger


register(BloggerFactory)
register(BlogFactory)


@pytest.fixture
def blog(blogger):
    return BlogFactory(blogger=blogger)


@pytest.fixture
def comment(blogger, blog):
    return CommentFactory(blog=blog, blogger=blogger)
