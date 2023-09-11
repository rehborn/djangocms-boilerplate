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

ORDERING_CHOICES = [
    ("name_asc", _("Name Ascending")),
    ("name_desc", _("Name Descending")),
    ("prio_asc", _("Priority Ascending")),
    ("prio_desc", _("Priority Descending")),
]

INFO_CHOICES = [
    ("email", _("email")),
    ("phone", _("Phone")),
    ("linkedin", "Linkedin"),
    ("xing", "XING"),
    ("link", _("Link")),
    ("other", _("Other")),
]

