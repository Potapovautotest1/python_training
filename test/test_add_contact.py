# -*- coding: utf-8 -*-
import unittest
import pytest
from model.contact import contact
from fixture.Appcontact import appcontact


@pytest.fixture()
def appc(request):
    fixture=appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_create_new_contact(appc):
    appc.open_home_page()
    appc.session.login(username="admin", password="secret")
    appc.contact.init_add_contact(contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivaniv", nickname="Vanz",
                         title="GRS", company="GRS", address="Linina 12", home_phonenumber="7894568548", mobile_phonenumber="4854689797", work="GRS",
                         faxnumber="12345678", email="Faoy@email/com", bday="8", bmonth="July", byear="2000", ayear="2025",
                         group="dfgkfgjk", address2="linina 56", phone2="lenina 78", notes="fdjgjkfsdgiorewjtliokefjdl"))
    appc.session.logout()






    


if __name__ == "__main__":
    unittest.main()
