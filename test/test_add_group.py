# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new_gr", header="new_H", footer="new_F"))
    app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


