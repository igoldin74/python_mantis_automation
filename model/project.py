from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    # redefined standard representation method for printing out group object in console:
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.description)

    # redefined standard equals method for comparing projects objects by their attributes (name&id):
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name \
               and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize