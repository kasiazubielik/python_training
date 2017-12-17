import re
from model.contact import Contact


def test_contact_info_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_from_edit_page)


def test_all_contacts_info_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact_from_home_page in contacts_from_home_page:
        index = contacts_from_home_page.index(contact_from_home_page)
        contact_info_from_db = contacts_from_db[index]
        assert clear(contact_from_home_page.firstname) == clear(contact_info_from_db.firstname)
        assert clear(contact_from_home_page.lastname) == clear(contact_info_from_db.lastname)
        assert clear(contact_from_home_page.address) == clear(contact_info_from_db.address)


def clear(s):
    return re.sub("[() -]", "", s)


def clear_emails(s):
    return re.sub("[() ]", "", s)


def merge_emails_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))