class Account(object):
    def __init__(self):
        self.name = ""
        self.bank = ""
        self.id = 0
        self.created = ""
        self.balance = 0
        self.updated = ""

class Payee(object):
    def __init__(self):
        self.name = ""
        self.id = 0

class Transaction(object):
    def __init__(self):
        self.description = ""
        self.id = 0
        self.account = Account()
        self.amount = 0
        self.payee = Payee()
        self.description = ""
        self.date_posted = ""
        self.date_initial = ""

    def new(self):
        #Pull incremental ID from database and add to local object instance.
        #Check in with database, double check before adding to account balance, sanitize data.
        print("stub")

    def get







