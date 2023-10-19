from django.urls import path

from blogs.views.blogs import blogs

urlpatterns = (
    [
        path("", blogs.IndexView.as_view(), name="index"),
        path("<int:pk>", blogs.DetailView.as_view(), name="detail"),
    ],
    "blogs",
)
