from django.urls import include, path

from .blogger import urlpatterns as account_urlpatterns

app_name = "blogs"

urlpatterns = [
    path("accounts/", include(account_urlpatterns)),
]
