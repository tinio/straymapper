from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings

# Admin autodiscover is no longer needed in modern Django
admin.autodiscover()

from animals import views as animal_views

urlpatterns = [
    re_path(r'^about/$', TemplateView.as_view(template_name='about.html')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    path('animals/', include('animals.urls')),
    path('report/', include('reports.urls')),

    re_path(r'^$', animal_views.index, name='home'),
]

# Add debug toolbar URLs in development
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
