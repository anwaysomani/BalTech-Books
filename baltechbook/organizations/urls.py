from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'team/$', views.team, name='team'),
    url(r'team/member/(?P<emp_id>\d+)/$', views.team_member, name='team-member'),
]
