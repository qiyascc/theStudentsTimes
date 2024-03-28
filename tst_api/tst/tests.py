from django.test import TestCase
from .models import Tst, Page
import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Testing Models
class TstModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tst.objects.create(editor="Test Editor", month=datetime.date(2024, 3, 1))

    def test_str(self):
        tst = Tst.objects.get(id=1)
        expected_object_name = f"{tst.month.year} - March"
        self.assertEquals(expected_object_name, str(tst))

class PageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        tst = Tst.objects.create(editor="Test Editor", month=datetime.date(2024, 3, 1))
        Page.objects.create(Tst=tst, title="Test Page", supervisor="Supervisor")

    def test_str(self):
        page = Page.objects.get(id=1)
        self.assertEquals(page.title, str(page))

# Testing Views
class TstViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Tst.objects.create(editor="Test Editor", month=datetime.date(2024, 3, 1))

    def test_list_years(self):
        """
        Ensure we can list years.
        """
        url = reverse('tst-list-years')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_year_detail(self):
        """
        Ensure we can retrieve a year's details.
        """
        url = reverse('tst-year', kwargs={'year': '2024'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
