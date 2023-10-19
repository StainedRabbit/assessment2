from django.urls import include, path

from .profile import urlpatterns as profile_urlpatterns
from blogs.views.bloggers import DetailView

urlpatterns = (
    [
        path("profile/", include(profile_urlpatterns)),
        path("<int:pk>", DetailView.as_view(), name="detail"),
    ],
    "blogger",
)
