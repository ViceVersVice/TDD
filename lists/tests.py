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

    def setUp(self):
        self.correct_list = List.objects.create()


    def test_uses_list_template(self):
        response = self.client.get(f"/some-view/{self.correct_list.id}/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_only_items_for_that_list(self):

        Item.objects.create(text="Item 1", list=self.correct_list)
        Item.objects.create(text="Item 2", list=self.correct_list)

        other_list = List.objects.create()
        Item.objects.create(text="Other Item 1", list=other_list)
        Item.objects.create(text="Other Item 2", list=other_list)

        response = self.client.get(f"/some-view/{self.correct_list.id}/")

        self.assertContains(response, "Item 1")
        self.assertContains(response, "Item 2")
        self.assertNotContains(response, "Other Item 1")
        self.assertNotContains(response, "Other Item 2")

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        this_list = List.objects.create()

        response = self.client.get(f"/some-view/{this_list.id}/")

        self.assertEqual(response.context["list"], this_list)

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
        list_ = List.objects.first()
        self.assertRedirects(response, f"/some-view/{list_.id}/")

class NewItemTest(TestCase):

    def test_can_save_POST_to_a_existing_list(self):
        other_list = List.objects.create()
        this_list = List.objects.create()

        response = self.client.post(f"/some-view/{this_list.id}/add-item",
                                    data={"item_text": "This item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "This item")
        self.assertEqual(this_list, new_item.list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        this_list = List.objects.create()

        response = self.client.post(f"/some-view/{this_list.id}/add-item",
                                    data={"item_text": "This item"})
        self.assertRedirects(response, f"/some-view/{this_list.id}/")
