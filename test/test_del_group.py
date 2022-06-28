from model.Group import group

def test_delete_first_group(app):
    if app.group.count()==0:
        app.group.create(group(name="dfgkfgjk"))
    old_list_group = app.group.get_list_group()
    app.group.delete_first_group()
    new_list_group = app.group.get_list_group()
    assert len(old_list_group) - 1 == len(new_list_group)
    old_list_group[0:1] = []
    assert old_list_group == new_list_group