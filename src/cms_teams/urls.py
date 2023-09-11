from django.urls import path

from .views import *

urlpatterns = [
   path('<slug:team>/<slug:member>/', MemberView.as_view(), name="team-member"),
   path('<slug:team>/', TeamView.as_view(), name="team"),
   path('', TeamsView.as_view(), name='teams'),
]
