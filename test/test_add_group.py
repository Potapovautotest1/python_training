# -*- coding: utf-8 -*-
import time
from model.Group import group


def test_add_group(app):
    app.group.create(group(name="dfgkfgjk", header="fdkjgdl", footer="fdgjldgj"))
    time.sleep(3)

def test_add_empty_group(app):
    app.group.create(group(name="", header="", footer=""))
    time.sleep(3)

