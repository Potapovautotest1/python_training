from model.Group import group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(group(name="new name"))
    app.session.logout()