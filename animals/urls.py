from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^messages/$', views.process_data, name='animals_process_data'),
    re_path(r'^view/(?P<aid>.*?)/$', views.view, name='animals_view'),
    re_path(r'^popup/(?P<id>.*?)/$', views.popup, name='animals_popup'),
    re_path(r'^$', views.index, name='animals_index')
]
