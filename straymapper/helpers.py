import csv

from django.conf import settings
from geopy.geocoders import GoogleV3


def geocode(query):
    # Raises geopy.exc.ConfigurationError when GOOGLE_API_KEY is not set.
    return GoogleV3(api_key=settings.GOOGLE_API_KEY).geocode(query)


def unicode_csv_reader(csv_data, dialect=csv.excel, **kwargs):
    # Uploaded files iterate as UTF-8 encoded bytes; decode for csv.reader.
    return csv.reader(utf_8_decoder(csv_data), dialect=dialect, **kwargs)


def utf_8_decoder(csv_data):
    for line in csv_data:
        yield line.decode('utf-8') if isinstance(line, bytes) else line
