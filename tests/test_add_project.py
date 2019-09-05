from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits *5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list_from_ui()
    project=Project(name=random_string("test", 15), description="test_description")
    app.project.create_new_project(project)
    new_project_list = app.project.get_project_list_from_ui()
    assert len(new_project_list) == len(old_project_list) + 1
    old_project_list.append(project)
    project_list_soap = app.soap.get_proj_list_from_api("administrator", "root")
    print(project_list_soap)
    assert sorted(project_list_soap, key=Project.id_or_max) == sorted(old_project_list, key=Project.id_or_max)





