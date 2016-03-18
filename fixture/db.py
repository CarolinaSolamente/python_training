import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True # сбрасываем кеш в БД

    def get_group_list(self):
        list = [] # инициализируем список
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row # создаем кортеж
                list.append(Group(id=str(id), name=name, header=header, footer=footer)) # создаем объект и помещаем его в список
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = [] # инициализируем список
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row # создаем кортеж
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname)) # создаем объект и помещаем его в список
        finally:
            cursor.close()
        return list

    def destroy(self): #зачистка
        self.connection.close()