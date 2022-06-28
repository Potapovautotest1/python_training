from model.Group import group


def test_edit_group(app):
    old_list_group = app.group.get_list_group()
    if app.group.count()==0:
        app.group.create(group(name="dfgkfgjk"))
    gr = group(name="My HEADER is very good")
    gr.id = old_list_group[0].id
    app.group.edit(gr)
    new_list_group = app.group.get_list_group()
    assert len(old_list_group) == len(new_list_group)
    old_list_group[0] = gr
    assert sorted(old_list_group, key=group.id_or_max)== sorted(new_list_group, key=group.id_or_max)