from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Blogger(AbstractUser):
    about_me = models.TextField(blank=True, null=True)  # model text field
    is_alive = models.BooleanField(default=True)
    # model boolean field with default value of TRUE

    class Meta:
        verbose_name = _("Blogger")  # human readable name for the model
        verbose_name_plural = _("Bloggers")  # plural form of the model
        default_related_name = "bloggers"  #

    def get_absolute_url(self):
        return reverse("blog:blogger:detail", kwargs={"pk": self.pk})
