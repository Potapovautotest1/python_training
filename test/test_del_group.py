from model.Group import group
from random import randrange

def test_delete_some_group(app):
    if app.group.count()==0:
        app.group.create(group(name="dfgkfgjk"))
    old_list_group = app.group.get_list_group()
    index = randrange(len(old_list_group))
    app.group.delete_group_by_index(index)
    new_list_group = app.group.get_list_group()
    assert len(old_list_group) - 1 == len(new_list_group)
    old_list_group[index:index+1] = []
    assert old_list_group == new_list_group