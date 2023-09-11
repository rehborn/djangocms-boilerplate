from django.db import models
from django.utils.translation import gettext_lazy as _


class UserSettings(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.key}"

    class Meta:
        verbose_name_plural = _("User Settings")
