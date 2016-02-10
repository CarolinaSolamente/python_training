from model.group import Group
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# def test_modify_group_name(app):
#     app.group.modify_first_group(Group(name="New group"))

def test_modify_group(app):
            app.session.login(username="admin", password="secret")
            app.group.modify_first_group(Group(name="New group"))
            app.session.logout()

# def test_modify_group_header(app):
#     app.group.modify_first_group(Group(header="New header"))
