from model.Group import group


def test_edit_group(app):
    if app.group.count()==0:
        app.group.create(group(name="dfgkfgjk"))
    app.group.edit(group(header="My HEADER is very good"))
