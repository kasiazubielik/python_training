# -*- coding: utf-8 -*-
from model.address import Address
from random import randrange


def test_modify_address_name(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname="test"))
    old_addresses = app.address.get_address_list()
    index = randrange(len(old_addresses))
    address = Address(firstname="New firstname")
    address.id = old_addresses[index].id
    app.address.modify_address_by_index(index, address)
    assert len(old_addresses) == app.address.count()
    new_addresses = app.address.get_address_list()
    old_addresses[index] = address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)



# def test_modify_address_email(app):
#     if app.address.count() == 0:
#         app.address.create(Address(firstname="test"))
#     old_addresses = app.address.get_address_list()
#     app.address.modify_first_address(Address(email="New email"))
#     new_addresses = app.address.get_address_list()
#     assert len(old_addresses) == len(new_addresses)
