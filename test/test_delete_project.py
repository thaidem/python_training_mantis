from model.project import Project
import random


def test_login(app):
    app.session.login("administrator", "root1")


def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.project.get_project_list()
    index = (random.choice(old_projects)).path
    app.project.delete_project_by_index(index)
