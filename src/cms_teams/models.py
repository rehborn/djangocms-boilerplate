from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from .choices import *


class Team(models.Model):
    title = models.CharField(max_length=30, verbose_name=_("Title"), help_text=_("used in menu"))
    name = models.CharField(max_length=60, blank=True, verbose_name=_("Team Name"))
    slug = models.SlugField(unique=True, blank=True, help_text=_("must be unique, will be generated by title"))

    description = models.TextField(blank=True, help_text=u"optional")
    menu = models.BooleanField(default=False, verbose_name=u"collapse users in menu")

    template = models.CharField(default="team.html", max_length=30, choices=TEAM_APP_TEMPLATES)
    ordering = models.CharField(choices=ORDERING_CHOICES, default='asc', max_length=12)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("team")
        verbose_name_plural = _("teams")


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    team = models.ManyToManyField(Team, related_name="members", blank=True)
    public = models.BooleanField(default=False)

    title = models.CharField(max_length=30, blank=True, verbose_name=_("professional title"))
    role = models.CharField(max_length=30, blank=True, verbose_name=_("role"))
    description = HTMLField(blank=True)
    photo = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL, related_name='photo')
    background = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL, related_name='background')

    priority = models.IntegerField(default=0, help_text=_("sort priority"))

    slug = models.SlugField(unique=True, blank=True,
                            help_text=_("must be unique, will be generated by combining first and last name"))

    def __str__(self):
        return f"{self.user.username}"


class UserMeta(models.Model):
    user = models.ForeignKey(User, related_name="meta", on_delete=models.CASCADE)
    info = models.CharField(max_length=16, choices=INFO_CHOICES)
    name = models.CharField(max_length=30, blank=True)
    value = models.CharField(max_length=255)
    priority = models.IntegerField(default=0, help_text=_("sort priority"))

    def __str__(self):
        return f"{self.get_info_display()}"

    class Meta:
        verbose_name = _("info")
        verbose_name_plural = _("infos")


class TeamPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=TEAM_PLUGIN_TEMPLATES)
    team = models.ForeignKey(Team, unique=False, blank=True, null=True, on_delete=models.CASCADE)


class MemberPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=MEMBER_PLUGIN_TEMPLATES)
    profile = models.ForeignKey(UserProfile, unique=False, blank=True, null=True, on_delete=models.CASCADE)
