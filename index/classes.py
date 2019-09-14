

import sqlite3
import json
import locale


locale.setlocale(locale.LC_ALL, '')


class myDataBase:
    def __init__(self):
        self.con = sqlite3.connect(r"index/info.db")
        self.cur = self.con.cursor()
        with open('index/json.txt') as file:
            self.validNames = json.load(file)

    def saveJSON(self):
        with open('index/json.txt', 'w') as file:
            json.dump(self.validNames, file)

    def printJSON(self):
        for i in self.validNames:
            print (i)

    def addValidName(self, x):
        self.validNames.append(x)
        self.saveJSON()

    def removeValidName(self, x):
        self.validNames.remove(x)
        #self.validNames
        self.saveJSON()

    def testing(self):
        return "test works"

    def viewAll(self, table):
        self.cur.execute("SELECT * FROM " + table)
        rows = self.cur.fetchall()
        return rows

    def viewOne(self, x):
        self.cur.execute("SELECT * FROM " + x)
        y = self.cur.fetchall()
        return y

# MAy not use - Just for master db of all movement
    def payBill(self, account, accType, name, bMonth, due, payDate, pay):
        x = (accounts.getAmount(self, account, accType))
        x = float(x[0][0])
        print(locale.currency(x - float(pay)))
        y = (x - float(pay))
        if y <= 0:
            print("Insufficient Funds")
        else:
            print("Pass Funds Test")
            self.cur.execute("INSERT INTO Bills VALUES (NULL,?,?,?,?,?)", (name, bMonth, due, payDate, pay))
            self.con.commit()


    def payBill2(self, account, accType, name, bMonth, due, payDate, pay):
        x = (accounts.getAmount(self, account, accType))
        x = float(x[0][0])
        print(locale.currency(x - float(pay)))
        y = (x - float(pay))
        if y <= 0:
            self.mes = "Insufficient Funds"
            self.mesTrigger = False
            print("Insufficient Funds")
        else:
            print("Pass Funds Test")
            self.mesTrigger = True
            self.cur.execute("INSERT INTO " + name + " VALUES (?,?,?,?)", (bMonth, due, payDate, pay))
            self.con.commit()
            accounts.updateAmount(self, y, account, accType)
            self.mes = "Payment Made"

    def makeDeposit(self, account, accType, notes, date, amount):
        x = (accounts.getAmount(self, account, accType))
        x = float(x[0][0])
        print(x)
        nAmount = x + float(amount)
        self.cur.execute("INSERT INTO deposits VALUES (?,?,?,?,?,?)", (account, accType, notes, date, amount, nAmount))
        self.con.commit()
        accounts.updateAmount(self, nAmount, account, accType)

    def deleteKey(self,x):
        self.cur.execute("DELETE FROM Bills WHERE Key = ?" , (x,))
        self.con.commit()


    def getMonthStatus(self, x, y):
        self.cur.execute("SELECT 'Bill Month' FROM " + x)
        x = self.cur.fetchall()
        print(y)
        print(x)

    def resetAll(self):
        print("DfdsfsdfdsF")
        for i in self.validNames:
            self.cur.execute("DELETE FROM " + i)
        self.cur.execute("DELETE FROM Bills")
        self.cur.execute("UPDATE accounts SET Amount = 0")
        self.con.commit()

    def __del__(self):
        self.con.close()


class accounts:
    def __init__(self):
        self.con = sqlite3.connect(r"index/info.db")
        self.cur = self.con.cursor()
        self.cur.execute("SELECT * FROM accounts")
        self.acc = self.cur.fetchall()

    def callData(self):
        self.cur.execute("SELECT * FROM accounts")
        self.acc = self.cur.fetchall()
        return self.acc

    def getAmount(self, y, z):
        self.cur.execute("SELECT Amount FROM accounts WHERE Name = ? AND Type = ?", (y, z))
        x = self.cur.fetchall()
        return x

    def updateAmount(self, x, y, z):
        self.cur.execute("UPDATE accounts SET Amount = ? WHERE Name = ? AND Type = ?", (x, y, z))
        self.con.commit()
        print("done")

    def __del__(self):
        self.con.close()
