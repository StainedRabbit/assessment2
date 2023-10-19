from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    blogger = models.ForeignKey("blogs.Blogger", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Blog")  # human readable name for the model
        verbose_name_plural = _("Blogs")  # plural form of the model
        default_related_name = "blogs"  #

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

    @property
    def create_comment_url(self):
        return reverse("blog:create", kwargs={"pk": self.pk})
