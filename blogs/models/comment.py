from django.db import models

from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    blogger = models.ForeignKey("blogs.Blogger", on_delete=models.CASCADE)
    blog = models.ForeignKey("blogs.Blog", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Comment")  # human readable name for the model
        verbose_name_plural = _("Comments")  # plural form of the model
        default_related_name = "comments"  #
