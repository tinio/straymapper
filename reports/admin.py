from django.contrib.gis import admin

from reports.models import Report


class ReportAdmin(admin.GISModelAdmin):
    list_display = ('id', 'name', 'missing_since', 'animal_type', 'sex')
    search_fields = ('name', 'description')
    ordering = ('-missing_since',)

admin.site.register(Report, ReportAdmin)
