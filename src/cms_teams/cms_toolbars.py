from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import gettext_lazy as _
from cms.utils.urlutils import admin_reverse


@toolbar_pool.register
class CMSConfigToolbar(CMSToolbar):
    def populate(self):
        self.toolbar.add_link_item(
            name=_('Teams'),
            url=admin_reverse('cms_teams_team_changelist'),
            position=5,
        )
