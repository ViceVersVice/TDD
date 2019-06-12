from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import SomeView

# Create your tests here.
class SomeTest(TestCase):

    def test_SomeView_return_correct_html(self):
        response = self.client.get("/some-view/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self):
        response = self.client.post("/some-view/",
                                    data={"item_text": "a new list item"})
        self.assertIn("a new list item", response.content.decode("utf8"))
        self.assertTemplateUsed(response, "home.html")
