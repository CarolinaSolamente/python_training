# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string  # содержит константы хранящие списки символов


# генератор случайных строк
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # это символы, которые будем use in random генир-й строке
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# теперь данные существуют сами по себе, вытащили их из функции
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

# тестовые данные будут передовать в качестве параметра (через group)
# кто их туда будет передовать, кончно тестовый фреймворк


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    #    group = Group(name="testN", header="fffdf", footer="test")
    app.group.create(group)
    #   app.session.logout()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
