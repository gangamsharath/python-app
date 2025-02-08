import sqlite3

# Data access layer, function to perform to CURD on DB
#custom module

# code first approach
# DB first approch
from emp import Emp

def connectDB():
    global conn
    conn=sqlite3.connect("C:\\py-tt\\Day-03\\database\\employees.db")
    global cursor
    cursor=conn.cursor()
    print("connected to database")

def createTable():
    try:
        cmd="create table emps(fname text,lname text,pay integer)"
        cursor.execute(cmd)
    except Exception as ex:
        print("Can not create table emps")

def insertEmp(emp):
    try:
        cmd="insert into emps values(?,?,?)"
        values=(emp.fname,emp.lname,emp.pay)
        cursor.execute(cmd,values)
        cursor.execute("commit")
        print("One Emp added into Database")
    except Exception as ex:
        print("Techinical Error while added employee, Try again !!")

def readEmp(Emp):
    cmd="select * from emps"
    data=cursor.execute(cmd)
    print(list(data))

def deleteEmp(Emp):
    try:
        cmd="delete from emps where fname = :first"
        cursor.execute(cmd,{'first':Emp.fname})
        cursor.execute("commit")
        print("One Emp deleted into Database")
    except Exception as ex:
        print("Techinical Error while deletd employee, Try again !!",ex)

#Test Code
print("working with SQLLite3")
connectDB()
#createTable()

emp1= Emp('Kiran','Kumar',50)
# emp2= Emp('Som','sh',10)
# insertEmp(emp1)
# insertEmp(emp2)
readEmp(emp1)

deleteEmp(emp1)
print("After delete")
readEmp(emp1)
#Close the connection and cursor to avoid memory leaks
cursor.close()
conn.close()
