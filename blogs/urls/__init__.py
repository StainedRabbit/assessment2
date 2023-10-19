# from django.urls import include, path

# from .blog import urlpatterns as blog_urlpatterns

# app_name = "blogs"

# urlpatterns = [
#     path("blog/", include(blog_urlpatterns)),
# ]
from django.urls import include, path

# from blogs.views.bloggers import IndexView
from .blogger import urlpatterns as blogger_urlpatterns
from .bloggers import urlpatterns as bloggers_urlpatterns
from .blogs import urlpatterns as blogs_urlpatterns

from blogs.views.home import IndexView
from blogs.views.blogs import comment, blogs

app_name = "blog"

urlpatterns = [
    path("blogger/", include(blogger_urlpatterns)),
    path("bloggers/", include(bloggers_urlpatterns)),
    path("blogs/", include(blogs_urlpatterns)),
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>", blogs.DetailView.as_view(), name="detail"),
    path("<int:pk>/create/", comment.CreateView.as_view(), name="create"),
]


# from django.urls import include, path

# from .account import urlpatterns as account_urlpatterns
# from .manage import urlpatterns as manage_urlpatterns

# app_name = "app"

# urlpatterns = [
#     path("account/", include(account_urlpatterns)),
#     path("manage/", include(manage_urlpatterns)),
# ]
