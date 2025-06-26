from django.contrib.gis.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust


class Animal(models.Model):
    TYPE_CHOICES = (
        (u'PUPPY', u'Puppy'),
        (u'KITTEN', u'Kitten'),
        (u'DOG', u'Dog'),
        (u'CAT', u'Cat'),
    )

    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'U', u'Unknown'),
    )

    animal_id = models.CharField(max_length=255)
    intake_date = models.DateField()
    location = models.CharField(max_length=255)
    intake_condition = models.CharField(max_length=255)
    animal_type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES)
    spayed = models.BooleanField('Spayed or Neutered', default=False)
    age = models.IntegerField('Age in Days')
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255)
    intake_total = models.IntegerField()
    outcome_type = models.CharField(max_length=255, blank=True, null=True)
    outcome_date = models.DateField(blank=True, null=True)
    transferred_to = models.CharField(max_length=255, blank=True, null=True)
    photo_updated = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='straymapper/photos', blank=True,
                              null=True)
    thumbnail = ImageSpecField(source='photo',
                               processors=[Adjust(contrast=1.2, sharpness=1.1),
                                         ResizeToFill(120, 90)],
                               format="JPEG", options={'quality': 90})

    # Temporarily commented out for testing without GIS
    # geometry = models.PointField(srid=4326)
    geometry = models.CharField(max_length=255, blank=True, null=True)  # Temporary replacement

    objects = models.Manager()  # GeoManager is deprecated, regular Manager now has GIS support

    def __str__(self):
        return self.animal_id

    def is_adoptable(self):
        return True if self.outcome_type == u'ADOPTION' else False

    def is_dog(self):
        return True if self.animal_type == u'DOG' else False
