from sys import maxsize

class contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home_phonenumber=None, mobile_phonenumber=None,
                 work=None, faxnumber=None, email=None, bday=None, bmonth=None, byear=None, ayear=None, group=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.home_phonenumber=home_phonenumber
        self.mobile_phonenumber=mobile_phonenumber
        self.work=work
        self.faxnumber=faxnumber
        self.email=email
        self.bday=bday
        self.bmonth=bmonth
        self.byear=byear
        self.ayear=ayear
        self.group=group
        self.address2=address2
        self.phone2=phone2
        self.notes=notes
        self.id=id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
