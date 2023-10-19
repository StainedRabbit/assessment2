import factory

from blogs.models import Comment


class CommentFactory(factory.django.DjangoModelFactory):
    blogger = factory.SubFactory("factories.BloggerFactory")
    blog = factory.SubFactory("factories.Blog")
    comment = factory.Sequence(lambda n: f"comment{n}")

    class Meta:
        model = Comment
