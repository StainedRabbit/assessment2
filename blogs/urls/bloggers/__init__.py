from django.urls import path

from blogs.views.bloggers import IndexView

urlpatterns = (
    [
        path("", IndexView.as_view(), name="index"),
    ],
    "bloggers",
)
