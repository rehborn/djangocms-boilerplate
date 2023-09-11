from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext as _

from cms_teams.models import TeamPlugin, MemberPlugin


@plugin_pool.register_plugin
class TeamPlugin(CMSPluginBase):
    model = TeamPlugin
    name = _("Team Plugin")
    render_template = 'cms_teams/plugin_team.html'

    def render(self, context, instance, placeholder):
        self.render_template = f"cms_teams/{instance.template}"
        context.update({'team': instance.team})
        return context


@plugin_pool.register_plugin
class MemberPlugin(CMSPluginBase):
    model = MemberPlugin
    name = _("Member Plugin")
    render_template = 'cms_teams/plugin_member.html'

    def render(self, context, instance, placeholder):
        self.render_template = f"cms_teams/{instance.template}"
        context.update({'profile': instance.profile})
        return context
