import pytest
from factories import BloggerFactory


from pytest_factoryboy import register

from blogs.models import Blogger


register(BloggerFactory)
