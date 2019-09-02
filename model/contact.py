from sys import maxsize


class Contact:

    def __init__(self, firstname=None,
                 lastname=None,
                 middlename=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 phone2=None,
                 email1=None,
                 email2=None,
                 email3=None,
                 all_emails=None,
                 all_phones=None,
                 address=None,
                 id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.phone2 = phone2
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails
        self.address = address
        self.all_phones = all_phones
        self.id = id

    def __repr__(self):     # redefined standard representation method for printing out contact object in console
        return "%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.all_emails, self.all_phones,
                                   self.homephone, self.email1)

    def __eq__(self, other):    # redefined standard equals method for comparing contact objects by their attributes
                                # (name&id)
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and \
               self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
