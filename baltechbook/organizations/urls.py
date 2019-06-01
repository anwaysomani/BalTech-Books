from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'team/$', views.team, name='team'),
    url(r'team/member/(?P<emp_id>[\w\-]+)/$', views.team_member, name='team-member'),
    url(r'new-distributor/$', views.distributor_registration, name='distributor-form'),
]
