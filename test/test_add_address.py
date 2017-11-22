# -*- coding: utf-8 -*-

from model.address import Address

    
def test_add_address(app):
    old_addresses = app.address.get_address_list()
    address = Address(firstname="Jan", middlename="P.", lastname="Kowalski", nickname="none", title="Mr.", company="none", address="ul. Polna 3 00-123 Warszawa",
                               home_phone="+22 0987867", mobile_phone="+48 765890765", work_phone="+48 564389067", fax="none", email="jan.kowalski@mail.com",
                               email2="jan.k@mymail.com", email3="j.kowalski.kowalski.com", homepage="www.jakowalski.com", birth_date="1981", address2="none", notes="none",
                               phone2="home")
    app.address.create(address)
    assert len(old_addresses) + 1 == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)


# def test_add_empty_address(app):
#     old_addresses = app.address.get_address_list()
#     app.address.create(Address(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="=", work_phone="", fax="", email="",
#                                email2="", email3="", homepage="", birth_date="", address2="", notes="", phone2=""))
#     new_addresses = app.address.get_address_list()
#     assert len(old_addresses) + 1 == len(new_addresses)
