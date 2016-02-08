
from model.group import Group

def test_modify_fist_group(app):
    app.group.modify_first_group(Group(name="name_modify", header="h_modify", footer="f_modify"))
