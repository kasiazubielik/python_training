# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.address import Address


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_address(app):
    app.login(username="admin", password="secret")
    app.create_address(Address(firstname="Jan", middlename="P.", lastname="Kowalski", nickname="none", title="Mr.", company="none", address="ul. Polna 3 00-123 Warszawa",
                            home_phone="+22 0987867", mobile_phone="+48 765890765", work_phone="+48 564389067", fax="none", email="jan.kowalski@mail.com",
                            email2="jan.k@mymail.com", email3="j.kowalski.kowalski.com", homepage="www.jakowalski.com", birth_date="1981", address2="none", notes="none",
                            phone2="home"))
    app.logout()

def test_add_empty_address(app):
    app.login(username="admin", password="secret")
    app.create_address(Address(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="=", work_phone="", fax="", email="",
                                  email2="", email3="", homepage="", birth_date="", address2="", notes="", phone2=""))
    app.logout()


