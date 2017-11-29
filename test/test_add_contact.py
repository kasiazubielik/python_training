# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", lastname="", address="",
                    home_phone="", mobile_phone="=", work_phone="",
                    email="", email2="", email3="", phone2="")] + [
            Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 10),
                               home_phone=random_string("home_phone", 10), mobile_phone=random_string("mobile_phone", 10),
                               work_phone=random_string("work_phone", 10), email=random_string("email", 10) + '@' + random_string("", 10),
                               email2=random_string("email2", 10) + '@' + random_string("", 10), email3=random_string("email3", 10) + '@' + random_string("", 10),
                               phone2=random_string("phone2", 10))
            for i in range(5)
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


