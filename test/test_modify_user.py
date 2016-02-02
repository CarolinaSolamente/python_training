from model.user import User

def test_modify_fist_user(app):
    app.session.login(username="admin", password="secret")
    app.user.modify_first_user()
    app.session.logout()