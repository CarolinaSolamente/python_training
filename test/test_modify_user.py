from model.user import User

def test_modify_fist_user(app):
    if app.user.count() == 0:
        app.user.create(User(fname="add_001", mname="2", lname="3", nname="4", title="5", company="6", address="7", home="8", mobile="9", twork="10", fax="11", email="1.32.@6.ru", email2="12", email3="13", homepage="14", byear="2000", ayear="2100", address2="15", phone2="16", notes="17"))
    app.user.modify_first_user(User(fname="mod_002", mname="m2", lname="m3", nname="m4", title="m5", company="m6", address="m7", home="m8", mobile="m9", twork="m10", fax="m11", email="m1.32.@6.ru", email2="m12", email3="m13", homepage="m14", byear="2100", ayear="2200", address2="m15", phone2="m16", notes="mod17"))
