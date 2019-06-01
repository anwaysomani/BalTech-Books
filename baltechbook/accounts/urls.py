from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    url(r'^panel-redirect/$' , PanelRedirectView.as_view() , name="panel-redirect"),
]
