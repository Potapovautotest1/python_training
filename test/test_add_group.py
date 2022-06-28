# -*- coding: utf-8 -*-
import time
from model.Group import group


def test_add_group(app):
    old_list_group = app.group.get_list_group()
    gr = group(name="dfgkfgjk", header="fdkjgdl", footer="fdgjldgj")
    app.group.create(gr)
    new_list_group = app.group.get_list_group()
    assert len(old_list_group)+1 == len(new_list_group)
    old_list_group.append(gr)
    assert sorted(old_list_group, key=group.id_or_max)== sorted(new_list_group, key=group.id_or_max)
    time.sleep(3)

def test_add_empty_group(app):
    old_list_group = app.group.get_list_group()
    gr = group(name="", header="", footer="")
    app.group.create(gr)
    new_list_group = app.group.get_list_group()
    assert len(old_list_group)+1 == len(new_list_group)
    old_list_group.append(gr)
    assert sorted(old_list_group, key=group.id_or_max) == sorted(new_list_group, key=group.id_or_max)
    time.sleep(3)

