

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

    def delete_new_project(self):
        pass

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
                self.project_cache.append(Project(id=proj_id, name=name, description=description))
        return list(self.project_cache)
