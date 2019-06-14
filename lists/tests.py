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

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get("/some-view/list1/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_all_items(self):
        Item.objects.create(text="Item 1")
        Item.objects.create(text="Item 2")

        response = self.client.get("/some-view/list1/")
        print(response.status_code)

        self.assertContains(response, "Item 1")
        self.assertContains(response, "Item 2")

class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        response = self.client.post("/some-view/new",
                                    data={"item_text": "a new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "a new list item")

    def test_redirects_after_POST(self):
        response = self.client.post("/some-view/new",
                                    data={"item_text": "a new list item"})
        self.assertRedirects(response, "/some-view/list1/")
