# from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Team


class TeamsView(TemplateView):
    template_name = 'cms_teams/teams.html'

    def get(self, request, *args, **kwargs):
        teams = Team.objects.all().order_by('slug')
        return render(request, self.template_name, context={'teams': teams})


class TeamView(TemplateView):
    template_name = 'cms_teams/team.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("team", None)
        team = get_object_or_404(Team, slug=slug)
        return render(request, self.template_name, context={'team': team})


class MemberView(TemplateView):
    template_name = 'cms_teams/member.html'

    def get(self, request, *args, **kwargs):
        team_slug = kwargs.get("team", None)
        member_slug = kwargs.get("member", None)
        team = get_object_or_404(Team, slug=team_slug)
        profile = team.members.get(slug=member_slug)

        if not profile.public:
            return Http404()

        context = {
            'team': team,
            'profile': profile,
            'meta': profile.user.meta.all().order_by("priority"),
            'meta_dict': [{obj.name: obj.value} for obj in profile.user.meta.all() if obj.name]
        }
        return render(request, self.template_name, context=context)
