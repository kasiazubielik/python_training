from model.group import Group
import random
# from random import randrange


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    # app.group.delete_group_by_index(index)
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    # index = random.randrange(len(old_groups))
    # app.group.delete_group_by_index(index)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # new_groups = db.get_group_list()
    # old_groups[index:index + 1] = []
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
