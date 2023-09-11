from django.apps import AppConfig


class DjangoCMSBase(AppConfig):
    name = 'base'
    verbose_name = "Django CMS Settings"

    def ready(self):
        super(DjangoCMSBase, self).ready()
        import base.signals  # noqa
