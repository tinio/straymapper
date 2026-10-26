import requests

from django.core.files.base import ContentFile
from django.db.models import Q

from animals.models import Animal


def run():
    for a in Animal.objects.filter(Q(photo=u'') | Q(photo_updated=True)):
        print(a.animal_id)
        filename = a.animal_id + '.jpg'
        s = 'https://citypetz.s3.amazonaws.com/images/' + filename
        print(s)

        r = requests.get(s)
        if r.status_code == 200 and r.content:
            a.photo.save(filename, ContentFile(r.content), save=True)
            a.photo_updated = False
            a.save()
            print("appended photo to animal")
            thumb_url = a.thumbnail.url
        else:
            print("missing photo for " + a.animal_id)
