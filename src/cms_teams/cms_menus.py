from django.utils.translation import gettext_lazy as _

from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu
from django.urls import reverse
from menus.base import NavigationNode
from .models import Team


@menu_pool.register_menu
class TeamMenu(CMSAttachMenu):
    name = _("Team Menu")

    def get_nodes(self, request):
        menu = []
        for team in Team.objects.all().order_by('title'):
            url = reverse('cms_teams:team', kwargs={'team': team.slug})
            menu.append(NavigationNode(team.title, url, f"team_{team.id}"))
        return menu


@menu_pool.register_menu
class TeamMenuWithMembers(CMSAttachMenu):
    name = _("Team Menu with Members Submenu")

    def get_nodes(self, request):
        menu = []

        for team in Team.objects.all().order_by('-title'):
            members = team.members.filter(public=True).order_by('priority')

            _url = reverse('cms_teams:team', kwargs={'team': team.slug})
            node = NavigationNode(team.title, _url, f"team_{team.id}")

            if team.menu and members.count() > 0:
                node.children = []
                for member in members:
                    __url = reverse('cms_teams:team-member', kwargs={'team': team.slug, 'member': member.slug})
                    sub_node = NavigationNode(member, __url, f"member_{member.id}", f"team_{team.id}")
                    node.children.append(sub_node)

            menu.append(node)

        return menu


@menu_pool.register_menu
class TeamMenuWithMembersCompact(CMSAttachMenu):
    name = _("Team Menu with Members only")

    def get_nodes(self, request):
        menu = []
        for team in Team.objects.all().order_by('title'):
            members = team.members.filter(public=True).order_by('priority')
            if team.menu and members.count() > 0:
                # url = reverse('cms_teams:team', kwargs={'team': team.slug})
                # menu.append(NavigationNode(team.title, url, team.id))
                for member in members:
                    __url = reverse('cms_teams:team-member', kwargs={'team': team.slug, 'member': member.slug})
                    menu.append(NavigationNode(member, __url, f"member_{member.id}"))

        return menu
