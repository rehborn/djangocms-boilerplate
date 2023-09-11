from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from modeltranslation.admin import TranslationAdmin

from .models import UserProfile, UserMeta, Team

admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1


class UserMetaInline(admin.TabularInline):
    model = UserMeta
    fk_name = 'user'
    extra = 0


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline, UserMetaInline]


class TeamMemberInline(admin.TabularInline):
    model = UserProfile.team.through
    extra = 0


@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    list_display = ['title', 'name', 'count_users']

    inlines = [TeamMemberInline]

    @staticmethod
    @admin.display(description=u"members")
    def count_users(obj):
        return obj.members.count()
