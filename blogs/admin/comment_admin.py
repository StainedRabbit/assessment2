from django.contrib import admin

from blogs.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
