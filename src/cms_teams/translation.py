from modeltranslation.translator import TranslationOptions, register
from .models import *


@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(UserProfile)
class MemberTranslationOptions(TranslationOptions):
    fields = ('title', 'role', 'description')
