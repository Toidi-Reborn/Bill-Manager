

from index.classes import myDataBase, accounts
import index.myVars
from tkinter import *
from tkinter import messagebox  #????  Not sure why it needs to be imported again??  maybe?
from tkinter.colorchooser import *
import time
import locale
import random
locale.setlocale(locale.LC_ALL, '')


def close():
    print("Program Closed by User")
    exit()


def clearBox():
    box1.delete(0, END)
    ifbox.delete(0, END)


def showDB():
    clearBox()
    dblist = data.viewAll()
    for i in dblist:
        box1.insert(END, i)


def showNames():
    clearBox()
    dblist = data.validNames
    for i in dblist:
        box1.insert(END, i)


def addBill():
    l2.config(text="")
    x = val1Value.get()
    if x != "":
        data.addValidName(x)
        val1.delete(0, END)
        l2.config(text=x + " has been added.")
    else:
        l2.config(text="Nothing Entered")
    showNames()


# No Longer Used
def todayAuto():
    now = time.localtime(time.time())
    nowX = str(now.tm_mon) + "/" + str(now.tm_mday) + "/" + str(now.tm_year)
    lg4b.delete(0, END)
    lg4b.insert(0, nowX)


def removeBill():
    l2.config(text="")
    x = val1Value.get()
    print(x)
    if x in data.validNames:
        data.removeValidName(x)
        val1.delete(0, END)
        l2.config(text=x + " has been removed.")
    elif x == "":
        l2.config(text="Nothing Entered")
    else:
        l2.config(text="Name Not Found")
        val1.delete(0, END)
    showNames()


def loadAccount():
    accounts.callData()
    x = accounts.acc
    rrow1a.config(text=x[0][0])
    rrow1b.config(text=x[0][1])
    rrow1c.config(text=locale.currency(x[0][2]))
#    rrow1c.config(text="$" + str(x[0][2]))
    rrow2a.config(text=x[1][0])
    rrow2b.config(text=x[1][1])
    rrow2c.config(text=locale.currency(x[1][2]))
    rrow3a.config(text=x[2][0])
    rrow3b.config(text=x[2][1])
    rrow3c.config(text=locale.currency(x[2][2]))
    rrow4a.config(text=x[3][0])
    rrow4b.config(text=x[3][1])
    rrow4c.config(text=locale.currency(x[3][2]))


def getAccountAndType(getAccountAndType):
    global account
    global accType

    if getAccountAndType == "Main - Checking":
        account = "Main"
        accType = "Checking"
    elif getAccountAndType == "Main - Savings":
        account = "Main"
        accType = "Savings"
    elif getAccountAndType == "House - Checking":
        account = "House"
        accType = "Checking"
    elif getAccountAndType == "House - Savings":
        account = "House"
        accType = "Savings"
    else:
        print("Error")


def payBill():
    global account
    global accType
    lg6.config(text="")
    billName = menuVar.get()
    bMonth = lg2_value.get()
    due = lg3_value.get()
    payDate = lg4_value.get()
    pay = lg5_value.get()
    payFrom = menuVar2.get()
    getAccountAndType(payFrom)

    if billName != "" and bMonth != "" and due != "" and payDate != "" and pay != "":
        print("Pass")
        if billName in data.validNames:
            print("Pass Bill Name Check")
            data.payBill(account, accType, billName, bMonth, due, payDate, pay)
            data.payBill2(account, accType, billName, bMonth, due, payDate, pay)
            loadAccount()
            lg6.config(text=data.mes, fg="red")
            print(data.mes)
            if data.mesTrigger:
                lg2b.delete(0, END)
                lg3b.delete(0, END)
                lg4b.delete(0, END)
                lg5b.delete(0, END)
                data.mesTrigger = False

        else:
            lg6.config(text="Bill Name Invalid", fg="red")
            print("Bill Name Invalid")
    else:
        lg6.config(text="Data Missing", fg="red")
        print("Data Missing")


def deposit():
    print("sadsad")
    global account
    global accType
    notes = dfi1_value.get()
    date = dfi2_value.get()
    amount = dfi3_value.get()
    payFrom = menuVar3.get()
    getAccountAndType(payFrom)
    data.makeDeposit(account, accType, notes, date, amount)
    loadAccount()


def showBill():
    clearBox()
    x = menuVar2dd.get()
    y = data.viewOne(x)
    for i in y:
        ifbox.insert(END, i)


def showDeposits():
    clearBox()
    masterList = data.viewAll("deposits")
    for i in masterList:
       ifbox.insert(END, i)


def showTrans():
    clearBox()
    masterList = data.viewAll("Bills")
    for i in masterList:
        ifbox.insert(END, i[1] + "   " + i[4] + "   " + locale.currency(i[5]))


def resetAll():
    if messagebox.askyesno("WARNING", "Are you sure you want to delete all data and set each account to $0?"):
        data.resetAll()
    else:
        print("Cancelled")


def infoMove():
    global moveing
    global movingColor
    x = random.randint(1,9)
    x = moving.get(x, "na")
    y = random.randint(1,9)
    y = movingColor.get(y, "na")
    z = random.randint(1,9)
    z = movingColor.get(z, "na")
    ifl1.config(bg=y)
    ifl1.config(anchor=x)
    ifl1.config(fg=z)
    window.after(500, infoMove)


def autoMonthDay():
    curTime = time.localtime(time.time())
    curMonth = int(curTime.tm_mon)
    curMonth = monthList.get(curMonth, "na")
    curMonth = curMonth + " " + str(curTime.tm_year)
    curDate = str(curTime.tm_mon) + "/" + str(curTime.tm_mday) + "/" + str(curTime.tm_year)
    lg2b.delete(0, END)
    lg4b.delete(0, END)
    lg2b.insert(0, curMonth)
    lg4b.insert(0, curDate)


def clock():
    now = time.localtime(time.time())
    timeM = " AM"

    timeHour = now.tm_hour
    if timeHour > 12:
        timeHour = now.tm_hour - 12
        timeM = " PM"
    timeMin = now.tm_min
    if timeMin < 10:
        timeMin = "0" + str(now.tm_min)
    timeSec = now.tm_sec
    if timeSec < 10:
        timeSec = "0" + str(now.tm_sec)

    now = str(now.tm_mon) + "/" + str(now.tm_mday) + "/" + str(now.tm_year) + " " + str(timeHour) + ":" + str(
        timeMin) + ":" + str(timeSec) + str(timeM)
    timeHold.config(text=now)
    window.after(1000, clock)


def getAColor():
    color = askcolor()
    print(color)
    b4.config(bg=color[1])



accounts = accounts()
data = myDataBase()
accounts.callData()
validNames = data.validNames

moving = index.myVars.moving
movingColor = index.myVars.movingColor
monthList = index.myVars.monthList


# print(data.testing())

print("\n")
print("\n")

window = Tk()
window.title("My Checkbook")
window.config(padx=20, pady=20)


# Frame initiation
infoFrame = Frame(window)
nameFrame = Frame(window)
nameFrame.config(height=500, width=500)
depositFrame = Frame(window)
leftFrame2 = Frame(window)
leftFrame2.config()
rightFrame = Frame(window)
rightFrame.config(bg="red", height=500)
leftMain = Frame(window)
leftMain.config(bg="blue", height=500)
topFrame = Frame(window)
topFrame.config(bg="white", height=10)
bottomFrame = Frame(window)
bottomFrame.config(bg="white", height=100, width=1000)

# Status Frame
statusFrame = Frame(window)
statusFrame.config(bg="silver", padx=10)
change = 0


# Frame Set
topFrame.grid(row=0, column=0, columnspan=2)
leftMain.grid(row=1, column=0)
leftFrame2.grid(row=2, column=0, pady=25)
depositFrame.grid(row=3, column=0)
# rightFrame.grid(row=1, column=2, rowspan=3)
infoFrame.grid(row=1, column=1, rowspan=2)
nameFrame.grid(row=3, column=1)
statusFrame.grid(row=0, column=2, rowspan=5)
bottomFrame.grid(row=4, column=0, columnspan=2)

# Top Frame

# Right Frame

l1r = Label(rightFrame, text="Debug Box")
l1r.grid(row=0, column=0)
box1 = Listbox(rightFrame, width=50, height=20)
box1.grid(row=1, column=0, pady=5, padx=5)
b1Right = Button(rightFrame, text="Clear Box", command=clearBox)
b1Right.grid(row=2, column=0)

b1Top = Button(rightFrame, text="View All in Database", command=showDB)
b1Top.grid(row=3, column=0, pady=5, padx=5)

b2Top = Button(rightFrame, text="View Valid Names", command=showNames)
b2Top.grid(row=3, column=1, pady=5, padx=5)

# Right Frame2

rowL = 10

rrA = Label(leftMain, bg="black", fg="white", text="Account", width=rowL)
rrA.grid(row=0, column=0)
rrB = Label(leftMain, bg="black", fg="white", text="Type", width=rowL)
rrB.grid(row=0, column=1)
rrC = Label(leftMain, bg="black", fg="white", text="Amount", width=rowL)
rrC.grid(row=0, column=2)

# Far Right Frame (Status)
sl1 = Label(statusFrame, text="Current Status")
sl1.grid(row=0, column=0)
for i in validNames:
    tempVar = "September 2019"
    changingLabel = Label(statusFrame, text=i)
    changingLabel.grid(row=change, column=0, sticky="e")
    data.getMonthStatus(i, tempVar)
    change += 1
















# Data
rrow1a = Label(leftMain, text="", width=rowL)
rrow1a.grid(row=1, column=0)
rrow1b = Label(leftMain, text="", width=rowL)
rrow1b.grid(row=1, column=1)
rrow1c = Label(leftMain, text="", width=rowL)
rrow1c.grid(row=1, column=2)

rrow2a = Label(leftMain, text="", width=rowL)
rrow2a.grid(row=2, column=0)
rrow2b = Label(leftMain, text="", width=rowL)
rrow2b.grid(row=2, column=1)
rrow2c = Label(leftMain, text="", width=rowL)
rrow2c.grid(row=2, column=2)

rrow3a = Label(leftMain, text="", width=rowL)
rrow3a.grid(row=3, column=0)
rrow3b = Label(leftMain, text="", width=rowL)
rrow3b.grid(row=3, column=1)
rrow3c = Label(leftMain, text="", width=rowL)
rrow3c.grid(row=3, column=2)

rrow4a = Label(leftMain, text="", width=rowL)
rrow4a.grid(row=4, column=0)
rrow4b = Label(leftMain, text="", width=rowL)
rrow4b.grid(row=4, column=1)
rrow4c = Label(leftMain, text="", width=rowL)
rrow4c.grid(row=4, column=2)

# Info Frame

ifl1 = Label(infoFrame, width=10, text="Info", bg="yellow", font=(None, 15))
ifl1.grid(row=0, column=0, columnspan=2, sticky="ew")
ifb1 = Button(infoFrame, text="Show Recent Payments", command=showTrans)
ifb1.grid(row=2, column=0, columnspan=1)
ifb2 = Button(infoFrame, text="Show Recent Deposits", command=showDeposits)
ifb2.grid(row=2, column=1)
ifbox = Listbox(infoFrame, width=50)
ifbox.grid(row=3, column=0, columnspan=2)
menuVar2dd = StringVar(infoFrame)
menuVar2dd.set("Menards")
ddown2 = OptionMenu(infoFrame, menuVar2dd, *validNames)
ddown2.grid(row=4, column=0)
ifb2 = Button(infoFrame, text="Show Bill Payments", command=showBill)
ifb2.grid(row=4, column=1)


# Name Frame

l1 = Label(nameFrame, text="Valid Bill Name Add/Remove")
val1Value = StringVar()
val1 = Entry(nameFrame, textvariable=val1Value)
b1 = Button(nameFrame, text="Add", width=7, command=addBill)
b2 = Button(nameFrame, text="Remove", width=7, command=removeBill)
l2 = Label(nameFrame, text="")
b3 = Button(nameFrame, text="Reset All", bg="red", fg="white", width=20, command=resetAll)
b4 = Button(nameFrame, text="Set the Color of this Button", command=getAColor)

l1.grid(row=0, column=0, columnspan=2, padx=5)
val1.grid(row=1, column=0, columnspan=2, padx=5)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
l2.grid(row=3, column=0, columnspan=2)
b3.grid(row=4, column=0, columnspan=2)
b4.grid(row=5, column=0, columnspan=2)


# Left Frame 2

timeHold = Label(leftFrame2, text="", fg="white", bg="teal")
timeHold.grid(row=0, column=0, columnspan=3, sticky="ew")

lg1 = Label(leftFrame2, text="Bill: ")
lg1.grid(row=3, column=0)
menuVar = StringVar(leftFrame2)
menuVar.set("")
ddown = OptionMenu(leftFrame2, menuVar, *validNames)
ddown.grid(row=3, column=1)

# lg1_value = StringVar()
# lg1b = Entry(leftFrame2, width=10, textvariable=lg1_value)
# lg1b.grid(row=3, column=1)

lg2 = Label(leftFrame2, text="Bill Month: ")
lg2.grid(row=4, column=0)
lg2_value = StringVar()
lg2b = Entry(leftFrame2, width=15, textvariable=lg2_value)
lg2b.grid(row=4, column=1)

lg3 = Label(leftFrame2, text="Due Date: ")
lg3.grid(row=5, column=0)
lg3_value = StringVar()
lg3b = Entry(leftFrame2, width=15, textvariable=lg3_value)
lg3b.grid(row=5, column=1)

lg4 = Label(leftFrame2, text="Date Paid: ")
lg4.grid(row=6, column=0)
lg4_value = StringVar()
lg4b = Entry(leftFrame2, width=15, text= "", textvariable=lg4_value)
lg4b.grid(row=6, column=1)
# lg4b2 = Button(leftFrame2, text="T", command=todayAuto)
# lg4b2.grid(row=6, column=2)
# Replaced with autoMonthDay

lg5 = Label(leftFrame2, text="Amount: ")
lg5.grid(row=7, column=0)
lg5_value = StringVar()
lg5b = Entry(leftFrame2, width=15, textvariable=lg5_value)
lg5b.grid(row=7, column=1)

menuVar2 = StringVar(leftFrame2)
menuVar2.set("Main - Checking")
ddown2 = OptionMenu(leftFrame2, menuVar2, "Main - Checking", "Main - Savings", "House - Checking", "House - Savings")
ddown2.grid(row=9, column=0, columnspan = 2)

billButton = Button(leftFrame2, text="Pay Bill", bg="red", fg="white", command=payBill)
billButton.grid(row=9, column=2, columnspan=1)

lg6 = Label(leftFrame2, text="")
lg6.grid(row=10, column=0, columnspan=3)


# Deposit Frame


df1 = Label(depositFrame, text="Deposit", fg="white", bg="black")
df1.grid(row=0, column=0, columnspan=2, sticky="ew")
df2 = Label(depositFrame, text="Reason: ")
df2.grid(row=1, column=0)
df3 = Label(depositFrame, text="Date: ")
df3.grid(row=2, column=0)
df4 = Label(depositFrame, text="Amount: ")
df4.grid(row=3, column=0)
df5 = Label(depositFrame, text="Account: ")
df5.grid(row=4, column=0)
menuVar3 = StringVar(depositFrame)
menuVar3.set("Main - Checking")
ddown3 = OptionMenu(depositFrame, menuVar3, "Main - Checking", "Main - Savings", "House - Checking", "House - Savings")
ddown3.grid(row=4, column=1)
dfi1_value = StringVar()
dfi2_value = StringVar()
dfi3_value = StringVar()
dfi1 = Entry(depositFrame, textvariable=dfi1_value)
dfi1.grid(row=1, column=1)
dfi2 = Entry(depositFrame, textvariable=dfi2_value)
dfi2.grid(row=2, column=1)
dfi3 = Entry(depositFrame, textvariable=dfi3_value)
dfi3.grid(row=3, column=1)
dfb1 = Button(depositFrame, command=deposit, fg="white", bg="green", text="Make Deposit")
dfb1.grid(row=5, column=0, columnspan=2)


# Bottom Frame


# set padding for name frame with for loop
for child in nameFrame.children.values():
    child.grid_configure(padx=5, pady=5)


exitApp = Button(bottomFrame, text="Close Application", bg="red", fg="yellow", command=close)
exitApp.grid(row=0, column=0, pady=10)

infoMove()
loadAccount()
clock()
autoMonthDay()

window.mainloop()