from zeep import Client, Settings
from model.project import Project
import re


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_proj_list_from_api(self, username, password):
        client = Client("http://localhost/mantis/api/soap/mantisconnect.php?wsdl")
        with client.settings(raw_response=False):
            result = client.service.mc_projects_get_user_accessible(username, password)
            project_list = []
            for element in result:
                project_list.append(Project(id=int(element.id), name=self.clear(element.name),
                                            description=self.clear(element.description)))
        return project_list

    def clear(self, s):
        if s is None:
            pass
        else:
            return re.sub("[() -]", "", s)





