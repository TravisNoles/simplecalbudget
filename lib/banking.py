class Bank(object):
    def __init__(self):
        self.name = ""
        self.created = ""

class Account(object):
    def __init__(self):
        self.name = ""
        self.created = ""
        self.balance = 0

class Payee(object):
    def __init__(self):
        self.name = ""

class Transaction(object):
    def __init__(self):
        self.name = ""
        self.account = Account()
        self.amount = 0
        self.payee = Payee()
        self.description = ""







