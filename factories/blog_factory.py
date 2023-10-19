import factory

from blogs.models import Blog


class BlogFactory(factory.django.DjangoModelFactory):
    blogger = factory.SubFactory("factories.BloggerFactory")
    title = factory.Sequence(lambda n: f"blog title{n}")
    content = factory.Sequence(lambda n: f"blog content{n}")
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = Blog
