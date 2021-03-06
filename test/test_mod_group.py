# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random


def test_modify_group_name(app, db, check_ui):
    if db.get_group_list == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group = Group(name="New group")
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)