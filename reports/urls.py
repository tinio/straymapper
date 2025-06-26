from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^view/(?P<id>.*?)/$', views.view, name='reports_view'),
    re_path(r'^$', views.index, name='reports_index')
]
