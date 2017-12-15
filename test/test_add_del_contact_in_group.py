# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm, check_ui):
    contact_list = orm.get_contact_list()
    if len(contact_list) == 0:
        app.contact.create(Contact(firstname="First", lastname="Last"))
        contact_list = orm.get_contact_list()
    contact = random.choice(contact_list)

    group_list = orm.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name="Name1", header="Header1", footer="Footer1"))
        group_list = orm.get_group_list()
    group = random.choice(group_list)
    contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    contacts_in_group.append(contact)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                              key=Contact.id_or_max)



def test_delete_contact_from_group(app, orm, check_ui):
    group_list = [i for i in orm.get_group_list() if i.name != ""]
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        group_list = orm.get_group_list()

    print("---------------")
    print(group_list)
    print("---------------")

    group = random.choice(group_list)
    contacts_in_group = orm.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        contact_list = orm.get_contact_list()
        if len(contact_list) == 0:
            app.contact.create(Contact(firstname="Name", lastname="Last"))
            contact_list = orm.get_contact_list()
        contact = random.choice(contact_list)
        app.contact.add_contact_to_group(contact, group)
        contacts_in_group = orm.get_contacts_in_group(group)
    else:
        app.contact.select_group(group)
    contact_to_delete = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact_to_delete, group)
    contacts_in_group.remove(contact_to_delete)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert sorted(contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


