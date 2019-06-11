from django.test import TestCase
from django.urls import resolve
from .views import SomeView
# Create your tests here.
class SomeTest(TestCase):

    def test_some_url(self):
        founded_view = resolve("/some-view/")
        self.assertEqual(SomeView, founded_view.func)
