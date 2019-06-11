from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import SomeView

# Create your tests here.
class SomeTest(TestCase):

    def test_some_url(self):
        founded_view = resolve("/some-view/")
        self.assertEqual(SomeView, founded_view.func)

    def test_SomeView_return_correct_html(self):
        request = HttpRequest()
        response = SomeView(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do</title>", html)
        self.assertTrue(html.endswith("</html>"))
