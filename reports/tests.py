import shutil
import tempfile
from io import BytesIO
from unittest import mock

from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse

from reports.models import Report

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ReportsViewsTestCase(TestCase):
    DATA = {'missing_since': '2026-10-20', 'location': '301 W 2nd St, Austin, TX',
            'animal_type': 'DOG', 'sex': 'Male', 'name': 'Buddy',
            'description': 'Brown lab mix', 'contact_info': 'call 555-0100'}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_form_renders(self):
        resp = self.client.get(reverse('reports_index'))
        self.assertContains(resp, 'id="report-form"')

    def test_invalid_submission_shows_errors(self):
        resp = self.client.post(reverse('reports_index'), {})
        self.assertContains(resp, 'errorlist')
        self.assertFalse(Report.objects.exists())

    @mock.patch('reports.models.geocode',
                return_value=('Austin, TX 78701, USA', (30.26, -97.74)))
    def test_submit_without_photo(self, geocode):
        resp = self.client.post(reverse('reports_index'), self.DATA)
        report = Report.objects.get()
        self.assertRedirects(resp, report.get_absolute_url())
        self.assertEqual(report.geometry, 'POINT (-97.74 30.26)')
        resp = self.client.get(report.get_absolute_url())
        self.assertContains(resp, 'Buddy')
        self.assertNotContains(resp, '/media/')

    @mock.patch('reports.models.geocode', side_effect=Exception('no key'))
    def test_submit_with_photo_when_geocoding_fails(self, geocode):
        buf = BytesIO()
        Image.new('RGB', (400, 300), (120, 80, 40)).save(buf, 'JPEG')
        photo = SimpleUploadedFile('dog.jpg', buf.getvalue(),
                                   content_type='image/jpeg')
        resp = self.client.post(reverse('reports_index'),
                                dict(self.DATA, photo=photo))
        report = Report.objects.get()
        self.assertRedirects(resp, report.get_absolute_url())
        self.assertIsNone(report.geometry)
        resp = self.client.get(report.get_absolute_url())
        self.assertContains(
            resp, '<img src="/media/straymapper/report-photos/dog')

    def test_missing_report(self):
        resp = self.client.get(reverse('reports_view', args=[999]))
        self.assertEqual(resp.status_code, 404)
