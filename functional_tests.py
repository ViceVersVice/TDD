from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000/some-view/')
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item",
        )
        inputbox.send_keys("Buy freedom")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(rows.text == "1: Buy freedom" for row in rows),
            "New to do item does not appear to be in html"
        )
        self.fail("Finish the Test!")
if __name__ == "__main__":
    unittest.main(warnings="ignore")