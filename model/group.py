from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):     # redefined standard representation method for printing out group object in console
        return "%s:%s:%s:%s" % (self.id, self.name, self.footer, self.header)

    def __eq__(self, other):    # redefined standard equals method for comparing group objects by their attributes
                                # (name&id)
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

