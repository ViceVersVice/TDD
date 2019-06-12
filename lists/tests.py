from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import SomeView
from lists.models import Item

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

class ItemModelTest(TestCase):

    def test_CR_item(self):
        first_item = Item.objects.create(text="Some 1 item")
        second_item = Item.objects.create(text="Some 2 item")

        all_items = Item.objects.all()
        self.assertEqual(2, all_items.count())
        first_saved_item = all_items[0]
        second_saved_item = all_items[1]
        self.assertEqual(first_saved_item.text, "Some 1 item")
        self.assertEqual(second_saved_item.text, "Some 2 item")
