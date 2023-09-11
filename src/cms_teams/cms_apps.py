from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _


@apphook_pool.register
class TeamAppHook(CMSApp):
    """CMS Teams Plugin App Hook"""
    app_name = "cms_teams"
    name = _("Teams AppHook")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["cms_teams.urls"]
