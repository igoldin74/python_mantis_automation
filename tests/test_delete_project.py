from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_delete_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list_from_ui()
    if len(old_project_list) == 0:
        app.project.create_new_project(Project(name=random_string("test", 10), description="test_description"))
        old_project_list = app.project.get_project_list_from_ui()
    project = random.choice(old_project_list)
    app.project.delete_project_by_id(project.id)
    old_project_list.remove(project)
    new_project_list = app.project.get_project_list_from_ui()
    assert sorted(new_project_list, key=Project.id_or_max) == sorted(old_project_list, key=Project.id_or_max)