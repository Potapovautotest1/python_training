# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.dv = webdriver.Firefox()
        self.dv.implicitly_wait(30)

    
    def test_add_group(self):
        dv = self.dv
        dv.get("http://localhost/addressbook/")
        dv.find_element_by_name("user").click()
        dv.find_element_by_name("user").clear()
        dv.find_element_by_name("user").send_keys("admin")
        dv.find_element_by_name("pass").clear()
        dv.find_element_by_name("pass").send_keys("secret")
        dv.find_element_by_id("LoginForm").submit()
        dv.find_element_by_link_text("groups").click()
        dv.find_element_by_name("new").click()
        dv.find_element_by_name("group_name").click()
        dv.find_element_by_name("group_name").clear()
        dv.find_element_by_name("group_name").send_keys("dfgkfgjk")
        dv.find_element_by_name("group_header").clear()
        dv.find_element_by_name("group_header").send_keys("fdkjgdl")
        dv.find_element_by_name("group_footer").clear()
        dv.find_element_by_name("group_footer").send_keys("fdgjldgj")
        dv.find_element_by_name("submit").click()
        dv.find_element_by_link_text("group page").click()
        dv.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.dv.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.dv.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.dv.quit()


if __name__ == "__main__":
    unittest.main()
