import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_list_contact()[0]
    contact_from_editpage = app.contact.get_info_contact_from_editpage(0)
    assert contact_from_homepage.firstname == clear(contact_from_editpage.firstname)
    assert contact_from_homepage.lastname == clear(contact_from_editpage.lastname)
    assert contact_from_homepage.id == clear(contact_from_editpage.id)
    assert contact_from_homepage.homephone == clear(contact_from_editpage.homephone)
    assert contact_from_homepage.mobilephone == clear(contact_from_editpage.mobilephone)
    assert contact_from_homepage.workphone == clear(contact_from_editpage.workphone)
    assert contact_from_homepage.faxphone == clear(contact_from_editpage.faxphone)

def clear(s):
    return re.sub("[() -]", "", s)


def test_phones_on_homepage(app):
    contact_from_viewpage = app.contact.get_list_contact_from_viewpage(0)
    contact_from_editpage = app.contact.get_info_contact_from_editpage_phone(0)
    assert contact_from_viewpage.firstname == contact_from_editpage.firstname
    assert contact_from_viewpage.lastname == contact_from_editpage.lastname
    assert contact_from_viewpage.id == contact_from_editpage.id
    assert contact_from_viewpage.homephone == contact_from_editpage.homephone
    assert contact_from_viewpage.mobilephone == contact_from_editpage.mobilephone
    assert contact_from_viewpage.workphone == contact_from_editpage.workphone
    assert contact_from_viewpage.faxphone == contact_from_editpage.faxphone




