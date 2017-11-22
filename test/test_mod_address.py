# -*- coding: utf-8 -*-

from model.address import Address


def test_modify_address_name(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname="test"))
    old_addresses = app.address.get_address_list()
    address = Address(firstname="New firstname")
    address.id = old_addresses[0].id
    app.address.modify_first_address(address)
    assert len(old_addresses) == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[0] = address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)



# def test_modify_address_email(app):
#     if app.address.count() == 0:
#         app.address.create(Address(firstname="test"))
#     old_addresses = app.address.get_address_list()
#     app.address.modify_first_address(Address(email="New email"))
#     new_addresses = app.address.get_address_list()
#     assert len(old_addresses) == len(new_addresses)
