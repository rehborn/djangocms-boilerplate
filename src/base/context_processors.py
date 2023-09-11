from django.conf import settings
from .models import UserSettings


def context_settings(request):
    _settings = {}
    for obj in UserSettings.objects.all():
        _settings[obj.key] = obj.value

    settings.user = _settings
    return {'settings': settings}
