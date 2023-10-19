import factory

from blogs.models import Blogger


class BloggerFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: f"test_email{n}@gmail.com")
    username = factory.Sequence(lambda n: f"username{n}")
    password = factory.Sequence(lambda n: f"password{n}")
    first_name = factory.Sequence(lambda n: f"first_name{n}")
    last_name = factory.Sequence(lambda n: f"last_name{n}")

    class Meta:
        model = Blogger
