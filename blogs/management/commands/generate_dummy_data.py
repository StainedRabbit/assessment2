from factories import BloggerFactory, BlogFactory
from django.core.management.base import BaseCommand
from django.db import transaction


@transaction.atomic
class Command(BaseCommand):
    help = "Generate dummy data"

    @transaction.atomic
    def generate_dummy_data(self):
        number_of_bloggers = 23
        number_of_blogs = 6
        for _ in range(number_of_bloggers):
            blogger = BloggerFactory()
            for _ in range(number_of_blogs):
                BlogFactory(blogger=blogger)

    def handle(self, *args, **kwargs):
        self.generate_dummy_data()
        print("Dummy data created.")
