from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import *


class Component(models.Model):
    component = models.CharField(max_length=50, unique=True, choices=COMPONENT_CHOICES)
    data = models.JSONField(default={})

    def __str__(self):
        return f"{self.component}"

    class Meta:
        verbose_name = _("Component")
        verbose_name_plural = _("Components")
