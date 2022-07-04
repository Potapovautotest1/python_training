import time
from model.contact import contact

def test_delete_first_contact(app):
    cntct = contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivaniv", nickname="Vanz",
                    title="GRS", company="GRS", address="Linina 12", home_phonenumber="7894568548",
                    mobile_phonenumber="4854689797", work="GRS",
                    faxnumber="12345678", email="Faoy@email/com", bday="8", bmonth="July", byear="2000", ayear="2025",
                    group="dfgkfgjk", address2="linina 56", phone2="lenina 78", notes="fdjgjkfsdgiorewjtliokefjdl")
    if app.contact.count_contact()==0:
        app.contact.init_add_contact(cntct)
    app.contact.open_contact_page()
    old_list = app.contact.get_list_contact()
    app.contact.delete_first_contact()
    time.sleep(5)
    app.contact.open_contact_page()
    new_list = app.contact.get_list_contact()
    assert len(old_list) == len(new_list)
    return sorted(old_list, key=contact.id_or_max) == sorted(new_list, key=contact.id_or_max)
    time.sleep(5)