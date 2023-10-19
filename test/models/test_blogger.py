import pytest
from factories import BloggerFactory


@pytest.mark.django_db
def test_blogger():
    normal_blogger = BloggerFactory(
        first_name="firstname", last_name="lastname", password="password"
    )
    assert normal_blogger.first_name == "firstname"
    assert normal_blogger.last_name == "lastname"
    assert normal_blogger.get_full_name() == "firstname lastname"
    assert normal_blogger.password == "password"
    assert normal_blogger.is_staff == False
    assert normal_blogger.is_superuser == False

    staff_blogger = BloggerFactory(is_staff=True)
    assert staff_blogger.is_staff == True
    assert staff_blogger.is_superuser == False

    superuser_blogger = BloggerFactory(is_superuser=True)
    assert superuser_blogger.is_staff == False
    assert superuser_blogger.is_superuser == True

    super_and_staff_blogger = BloggerFactory(is_superuser=True, is_staff=True)
    assert super_and_staff_blogger.is_staff == True
    assert super_and_staff_blogger.is_superuser == True
