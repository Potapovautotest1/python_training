# -*- coding: utf-8 -*-
import unittest, time
from model.Group import group
from fixture.Application import application
import pytest


@pytest.fixture()
def app(request):
    fixture=application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name_group="dfgkfgjk", header="fdkjgdl", footer="fdgjldgj"))
    app.session.logout()
    time.sleep(3)

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name_group="", header="", footer=""))
    app.session.logout()
    time.sleep(3)

if __name__ == "__main__":
    unittest.main()
