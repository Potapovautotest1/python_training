from model.Group import group
from random import randrange


def test_edit_group_by_index(app):
    if app.group.count()==0:
        app.group.create(group(name="dfgkfgjk"))
    old_list_group = app.group.get_list_group()
    index = randrange(len(old_list_group))
    gr = group(name="My HEADER is very good")
    gr.id = old_list_group[index].id
    app.group.edit_by_index(index, gr)
    new_list_group = app.group.get_list_group()
    assert len(old_list_group) == len(new_list_group)
    old_list_group[index] = gr
    assert sorted(old_list_group, key=group.id_or_max)== sorted(new_list_group, key=group.id_or_max)