from django.contrib import admin

from blogs.models import Blogger


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass
