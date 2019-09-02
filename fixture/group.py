from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        self.select_group_by_index(0)
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()
        self.group_cache = None

    def modify_group_by_id(self, group, group_id):
        wd = self.app.wd
        self.select_group_by_id(group_id)
        wd.find_element_by_name("edit").click()
        self.fill_out_group_form(group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()
        self.group_cache = None

    def modify_first_group(self, group):
        self.modify_group_by_index(group, 0)

    # def select_first_group(self):
    #     wd = self.app.wd
    #     wd.find_element_by_xpath("//input[@name='selected[]']").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//input[@name='selected[]']")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def fill_out_group_form(self, group):
        self.app.type("group_name", group.name)
        self.app.type("group_header", group.header)
        self.app.type("group_footer", group.footer)

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_xpath("//input[@name='selected[]']"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                group_id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=group_id))
        return list(self.group_cache)

