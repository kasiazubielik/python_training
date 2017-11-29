# -*- coding: utf-8 -*-

from model.contact import Contact

    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Jan", middlename="P.", lastname="Kowalski", nickname="none", title="Mr.", company="none", address="ul. Polna 3 00-123 Warszawa",
                               home_phone="+22 0987867", mobile_phone="+48 765890765", work_phone="+48 564389067", fax="none", email="jan.kowalski@mail.com",
                               email2="jan.k@mymail.com", email3="j.kowalski.kowalski.com", homepage="www.jakowalski.com", birth_date="1981", address2="none", notes="none",
                               phone2="(22)670-85-33")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="=", work_phone="", fax="", email="",
#                                email2="", email3="", homepage="", birth_date="", address2="", notes="", phone2=""))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
