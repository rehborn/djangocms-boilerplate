from django.conf import settings
from .models import UserSettings
from .config import _config


def context_settings(request):
    _settings = {}
    for obj in UserSettings.objects.all():
        _settings[obj.key] = obj.value

    settings.user = _settings
    settings.config = _config
    return {'settings': settings}
