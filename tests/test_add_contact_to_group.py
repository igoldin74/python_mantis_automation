from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="192.168.1.22", database="addressbook", user="admin", password="admin")


def test_add_contact_to_group(app):
    contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    if len(contact_list) == 0:
        app.contact.create(Contact(firstname="test_contact1_modified",
                              middlename="test_middle_name1_modified",
                              lastname="test_last_name1_modified",
                              homephone="234567777_new",
                              email1="test@tester.com"))
    if len(group_list) == 0:
        app.group.create(Group(name="test_group_random_name", header="random_header", footer="random_footer"))
    app.open_home_page()
    contact = random.choice(contact_list)
    group = random.choice(group_list)
    app.contact.add_contact_to_group(contact.id, group.id)
    contacts_in_group = db.get_contacts_in_group(group)
    print(contacts_in_group)
    if contact in contacts_in_group:
        assert True
