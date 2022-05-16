import sqlite3

class DBConnection():
    def __init__(self):
        self.con = sqlite3.connect('maindb.sqlite')
        self.cur = self.con.cursor()


    def newDB(self):
        """Initialize a new database with default values."""

        # Create Account Table
        self.cur.execute('''CREATE TABLE accounts
        (id, name, bank, created, balance, updated''')

        # Create Transactions Table
        self.cur.execute(''' CREATE TABLE transactions
        (id, date, desc, payee, posted''')


    def getTransaction(self):
        #for row in self.cur.execute('SELECT * FROM ')
        self.con.commit()
        self.con.close()

