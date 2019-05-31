from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'team/$', views.team, name='team'),
    url(r'team/member/<emp_id>/$', views.team_member, name='team-member'),
]
