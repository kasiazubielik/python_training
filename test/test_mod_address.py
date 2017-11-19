# -*- coding: utf-8 -*-

from model.address import Address


def test_modify_address_name(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname="test"))
    old_addresses = app.address.get_address_list()
    app.address.modify_first_address(Address(firstname="New firstname"))
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)


def test_modify_address_email(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname="test"))
    old_addresses = app.address.get_address_list()
    app.address.modify_first_address(Address(email="New email"))
    new_addresses = app.address.get_address_list()
    assert len(old_addresses) == len(new_addresses)
