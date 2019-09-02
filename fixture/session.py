

class SessionHelper:

    def __init__(self, app, baseurl):
        self.app = app
        self.baseurl = baseurl

    def login(self, username=None, password=None):
        wd = self.app.wd
        wd.get(self.baseurl)
        self.app.type("username", username)
        self.app.type("password", password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text == username

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

