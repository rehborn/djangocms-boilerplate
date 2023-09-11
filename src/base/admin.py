from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import UserSettings
from .config import config


class UserSettingAdmin(admin.ModelAdmin):
    list_display = ('get_setting_name', 'get_key', 'value')
    search_fields = ('key', 'value',)
    exclude = ['key']

    @staticmethod
    def get_setting_name(obj):
        return config('user_settings')[obj.key]

    def get_key(self, obj):
        return mark_safe(f"<code>{obj.key}</code>")

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(UserSettings, UserSettingAdmin)
