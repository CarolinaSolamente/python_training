# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    app.user.create(User(fname="103", mname="2", lname="3", nname="4", title="5", company="6", address="7", home="8", mobile="9", twork="10", fax="11", email="1.32.@6.ru", email2="12", email3="13", homepage="14", byear="2000", ayear="2100", address2="15", phone2="16", notes="17"))
    app.session.logout()

