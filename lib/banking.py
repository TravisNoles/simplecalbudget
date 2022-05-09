class Bank(object):
    def __init__(self):
        self.id = 0
        self.name = ""
        self.created = ""

class Account(object):
    def __init__(self):
        self.name = ""
        self.id = 0
        self.created = ""
        self.balance = 0


    def addtransactiontobal(self, trans_id, amount):
        self.balance = self.balance + amount

class Payee(object):
    def __init__(self):
        self.name = ""
        self.id

class Transaction(object):
    def __init__(self):
        self.name = ""
        self.id = 0
        self.account = Account()
        self.amount = 0
        self.payee = Payee()
        self.description = ""

    def new(self):
        #Pull incremental ID from database and add to local object instance.
        #Check in with database, double check before adding to account balance, sanitize data.
        print("stub")

    def get







