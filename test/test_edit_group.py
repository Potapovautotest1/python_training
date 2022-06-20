from model.Group import group


def test_edit_group(app):
    app.group.edit(group(name="new name"))
