# -*- coding: utf-8 -*-

from model.address import Address


def test_modify_address_name(app):
    app.address.modify_first_address(Address(firstname="New first name"))


def test_modify_address_email(app):
    app.address.modify_first_address(Address(email="New email"))
