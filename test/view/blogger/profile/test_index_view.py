import pytest

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from rest_framework import status


@pytest.mark.django_db
def test_index_view(client, blogger):
    url = reverse("blogs:blogger:profile:index")
    # test redirect to login page
    response = client.get(url, follow=True)
    assertTemplateUsed(response, "account/login.html")
    # test blogger login
    client.force_login(blogger)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assertTemplateUsed(response, "blogs/blogger/profile/index.html")
