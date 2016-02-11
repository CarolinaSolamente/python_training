from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
            app.group.create(Group(name="add_gr", header="f", footer="t"))
    app.group.delete_first_group()
