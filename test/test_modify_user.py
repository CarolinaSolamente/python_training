from model.user import User

def test_modify_fist_user(app):
    app.user.modify_first_user(User(fname="mod102", mname="m2", lname="m3", nname="m4", title="m5", company="m6", address="m7", home="m8", mobile="m9", twork="m10", fax="m11", email="m1.32.@6.ru", email2="m12", email3="m13", homepage="m14", byear="2100", ayear="2200", address2="m15", phone2="m16", notes="mod17"))
