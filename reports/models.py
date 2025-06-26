from geopy.geocoders import GoogleV3

from django.contrib.gis.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

g = GoogleV3(api_key='AIzaSyAZoNPSlRTETltbmJvgYYqol0SLAVBgKs')


class Report(models.Model):
    TYPE_CHOICES = (
        (u'DOG', u'Dog'),
        (u'CAT', u'Cat'),
    )

    GENDER_CHOICES = (
        (u'Male', u'Male'),
        (u'Female', u'Female'),
    )

    missing_since = models.DateField()
    location = models.CharField(max_length=255)
    animal_type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    sex = models.CharField(max_length=255, choices=GENDER_CHOICES)
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='straymapper/report-photos',
                              blank=True, null=True)
    thumbnail = ImageSpecField(source='photo',
                               processors=[Adjust(contrast=1.2, sharpness=1.1),
                                         ResizeToFill(120, 90)],
                               format="JPEG", options={'quality': 90})

    # Temporarily commented out for testing without GIS
    # geometry = models.PointField(srid=4326, null=True, blank=True)
    geometry = models.CharField(max_length=255, blank=True, null=True)  # Temporary replacement

    objects = models.Manager()  # GeoManager is deprecated, regular Manager now has GIS support

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('reports_view', args=[str(self.id)])

    def save(self, *args, **kwargs):
        location_changed = False
        if self.id:
            #TODO: copy values in init, since this is an extra db hit
            orig_self = Report.objects.get(id=self.id)
            if orig_self.location != self.location:
                location_changed = True
        if location_changed or not self.id:
            try:
                (place, point) = g.geocode(self.location)
            except:
                print("Location not found for report %s" % self.id)
            else:
                self.geometry = "POINT (%s %s)" % (point[1], point[0])
        return super(Report, self).save(*args, **kwargs)
