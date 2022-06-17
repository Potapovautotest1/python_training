# -*- coding: utf-8 -*-
import time
from model.Group import group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="dfgkfgjk", header="fdkjgdl", footer="fdgjldgj"))
    app.session.logout()
    time.sleep(3)

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="", header="", footer=""))
    app.session.logout()
    time.sleep(3)

