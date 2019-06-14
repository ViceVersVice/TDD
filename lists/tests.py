from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import SomeView
from lists.models import Item, List

# Create your tests here.
class SomeTest(TestCase):

    def test_SomeView_return_correct_html(self):
        response = self.client.get("/some-view/")
        self.assertTemplateUsed(response, "home.html")

class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_item(self):
        list_ = List()
        list_.save()

        first_item = Item.objects.create(text="Some 1 item", list=list_)
        second_item = Item.objects.create(text="Some 2 item", list=list_)

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)



        all_items = Item.objects.all()
        self.assertEqual(2, all_items.count())
        first_saved_item = all_items[0]
        second_saved_item = all_items[1]
        self.assertEqual(first_saved_item.text, "Some 1 item")
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, "Some 2 item")
        self.assertEqual(first_saved_item.list, list_)

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get("/some-view/list1/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text="Item 1", list=list_)
        Item.objects.create(text="Item 2", list=list_)

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
