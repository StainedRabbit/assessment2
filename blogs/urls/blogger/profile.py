from django.urls import path

from blogs.views.blogger import profile

urlpatterns = (
    [
        path("", profile.IndexView.as_view(), name="index"),
    ],
    "profile",
)
