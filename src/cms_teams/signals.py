from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from menus.menu_pool import menu_pool

from .models import Team, UserProfile


@receiver(post_save, sender=UserProfile)
@receiver(post_save, sender=Team)
def invalidate_menu(sender, **kwargs):
    # invalidate menu cache
    menu_pool.clear()


@receiver(post_save, sender=User)
def update_slug_on_user_update(sender, instance, **kwargs):
    profile, created = UserProfile.objects.get_or_create(user=instance)
    profile.slug = instance.username
    if instance.first_name or instance.last_name:
        profile.slug = slugify(f"{instance.first_name}-{instance.last_name}")
    profile.save()


@receiver(pre_save, sender=UserProfile)
def update_slug_on_profile_update(sender, instance, **kwargs):
    instance.slug = instance.user.username
    if instance.user.first_name or instance.user.last_name:
        instance.slug = slugify(f"{instance.user.first_name}-{instance.user.last_name}")
