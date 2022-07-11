from model.contact import contact
from random import randrange


def test_edit_contact_by_index(app):
    cntct = contact(firstname="Ferro", middlename="Markovich", lastname="Lorens", nickname="LOLO",
                    title="ABS", company="BSS", address="Rizskaia", home_phonenumber="7894568548",
                    mobile_phonenumber="4854689797", work="GRS",
                    faxnumber="12345678", email="Faoy@email/com", bday="8", bmonth="July", byear="2000", ayear="2025",
                    group="dfgkfgjk", address2="linina 56", phone2="lenina 78", notes="fdjgjkfsdgiorewjtliokefjdl")
    if app.contact.count_contact() == 0:
        app.contact.init_add_contact(cntct)
    old_list = app.contact.get_list_contact()
    edit_cntct = contact(firstname="Leonid", middlename="Grigoriev", lastname="Sergeevich", nickname="GRIGOR",
                    title="Lion")
    index = randrange(len(old_list))
    app.contact.edit_by_index(index, edit_cntct)
    new_list = app.contact.get_list_contact()
    assert len(old_list) == len(new_list)
    return sorted(old_list, key=contact.id_or_max) == sorted(new_list, key=contact.id_or_max)