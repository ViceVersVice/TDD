from django.test import TestCase
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

import unittest
import time
import os

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = "olek-kh-staging.tk:8000" #os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = "http://" + staging_server

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        MAX_WAIT = 10
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                # print(self.assertIn(row_text, [row.text for row in rows]),
                #       row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e# -*- coding: utf-8 -*-
                time.sleep(0.5)


    def test_can_start_a_list_for_one_user(self):

        self.browser.get(f"{self.live_server_url}/some-view/")
        print("URLLLL", f"{self.live_server_url}/some-view/")
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
        self.wait_for_row_in_list_table("1: Buy freedom")

        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy will")
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table("2: Buy will")
        self.wait_for_row_in_list_table("1: Buy freedom")

    def test_multiple_users_can_start_list_at_different_urls(self):
        # second user enters
        self.browser.get(f"{self.live_server_url}/some-view/")
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy will (second user)")
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table("1: Buy will (second user)")
        second_user_list_url = self.browser.current_url
        self.assertRegex(second_user_list_url, r"some-view/.+")

        # third user enters
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(f"{self.live_server_url}/some-view/")

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn("Buy will (second user)", page_text)
        self.assertNotIn("some shit", page_text)

        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Buy will (third user)")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy will (third user)")

        third_user_list_url = self.browser.current_url
        self.assertRegex(third_user_list_url, r"some-view/.+")
        self.assertNotEqual(second_user_list_url, third_user_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn("Buy will (second user)", page_text)
        self.assertIn("Buy will (third user)", page_text)
# if __name__ == "__main__":
#     unittest.main(warnings="ignore")
