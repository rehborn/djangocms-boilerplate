from django.utils.translation import gettext as _

TEAM_APP_TEMPLATES = [
    ("team.html", "Team"),
]

TEAM_PLUGIN_TEMPLATES = [
    ("plugin_team.html", "Team"),
]

MEMBER_PLUGIN_TEMPLATES = [
    ("plugin_member.html", "Member"),
]

INFO_CHOICES = [
    ("email", _("email")),
    ("phone", _("Phone")),
    ("linkedin", "Linkedin"),
    ("xing", "XING"),
    ("link", _("Link")),
    ("other", _("Other")),
]

