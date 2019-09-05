import random
import re
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_all_projects_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/manage_proj_page.php"):
            return
        wd.find_element_by_link_text("Manage Projects").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.app.navigation.open_manage_page()
        self.open_all_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_out_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def delete_random_project(self):
        wd = self.app.wd
        self.app.navigation.open_manage_page()
        self.open_all_projects_page()
        projects = wd.find_elements_by_css_selector('[href*="manage_proj_edit_page.php?project_id="]')
        random.choice(projects).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_manage_page()
        self.open_all_projects_page()
        self.select_project_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('[href="manage_proj_edit_page.php?project_id=%s"]' % id).click()

    def fill_out_project_form(self, project):
        self.app.type("name", project.name)
        self.app.type("description", project.description)

    project_cache = None

    def get_project_list_from_ui(self):
        self.app.navigation.open_manage_page()
        self.open_all_projects_page()
        if self.project_cache is None:
            wd = self.app.wd
            self.open_all_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("table.width100 tbody [class='row-1'], table.width100 tbody [class='row-2']"):
                proj_id = int(element.find_element_by_css_selector('[href*="manage_proj_edit_page.php?project_id="]')
                         .get_attribute('href')[-2:].replace('=', '0'))
                name = element.find_element_by_css_selector('td:nth-of-type(1)').text
                description = element.find_element_by_css_selector('td:nth-of-type(5)').text
                if description == "":
                    description = None
                self.project_cache.append(Project(id=proj_id, name=self.clear(name), description=self.clear(description)))
        return list(self.project_cache)

    def clear(self, s):
        if s is None:
            pass
        else:
            return re.sub("[() -]", "", s)