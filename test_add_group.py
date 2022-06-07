# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
from Group import group
from Application import application
import pytest


@pytest.fixture()
def app(request):
    fixture=application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.init_create_new_group(group(name_group="dfgkfgjk", header="fdkjgdl", footer="fdgjldgj"))
    app.logout()
    time.sleep(3)

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.init_create_new_group(group(name_group="", header="", footer=""))
    app.logout()
    time.sleep(3)



if __name__ == "__main__":
    unittest.main()
