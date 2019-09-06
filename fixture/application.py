from selenium import webdriver
from fixture.session import SessionHelper
from fixture.navigation import NaviHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self, baseurl=config["web"]["base_url"])
        self.navigation = NaviHelper(self)
        self.project = ProjectHelper(self)
        # Passing config file to application:
        self.config = config
        self.soap = SoapHelper(self)

    def destroy(self):
        self.wd.quit()

    def type(self, field_name, text):
            wd = self.wd
            if text is not None:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)

    def is_not_valid(self):
        try:
            self.wd.current_url
            return False
        except:
            return True
