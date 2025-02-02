import sqlite3
#data access layer functions to perform crud on db
#code 1st approach
#db 1st approach
from employee import Employee

def connectDB():
    global conn
    conn=sqlite3.connect("employes.db")
    global cursor
    cursor=conn.cursor
    print("connected to database")

def connectDB():
    pass
def createTable():
    pass
def insertEmp(emp):
    pass
def readEmp(emp):
    pass
def deleteEmp(emp):
    pass

#test code
print("working with sqlite3 database")
#connect to db
connectDB()


