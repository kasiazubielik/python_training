# -*- coding: utf-8 -*-

from model.address import Address


def test_modify_first_address(app):
    app.session.login(username="admin", password="secret")
    app.address.modify_first_address(
        Address(firstname="edited Jan", middlename="edited P.", lastname="edited Kowalski", nickname="edited none", title="edited Mr.", company="edited none",
                address="edited ul. Polna 3 00-123 Warszawa",
                home_phone="edited +22 0987867", mobile_phone="edited +48 765890765", work_phone="edited +48 564389067", fax="edited none",
                email="edited jan.kowalski@mail.com",
                email2="edited jan.k@mymail.com", email3="edited j.kowalski.kowalski.com", homepage="edited www.jakowalski.com",
                birth_date="edited 1981", address2="edited none", notes="edited none",
                phone2="edited home"))
    app.session.logout()
