
from model.group import Group

def test_modify_fist_group(app):
     if app.group.count() == 0:
            app.group.create(Group(name="add_gr", header="f", footer="t"))
     app.group.modify_first_group(Group(name="modify_gr", header="h_modify", footer="f_modify"))
