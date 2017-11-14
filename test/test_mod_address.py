# -*- coding: utf-8 -*-

from model.address import Address


def test_modify_address_name(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname="test"))
    app.address.modify_first_address(Address(firstname="New firstname"))


def test_modify_address_email(app):
    if app.address.count() == 0:
        app.address.create(Address(firstname="test"))
    app.address.modify_first_address(Address(email="New email"))
