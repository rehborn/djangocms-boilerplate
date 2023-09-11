from django.apps import AppConfig


class DjangoCMSTeams(AppConfig):
    name = 'cms_teams'
    verbose_name = "Django CMS Teams"

    def ready(self):
        super(DjangoCMSTeams, self).ready()
        import cms_teams.signals  # noqa
