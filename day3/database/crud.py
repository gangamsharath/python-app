import sqlite3
#data access layer functions to perform crud on db
#code 1st approach
#db 1st approach
from employee import Employee

def connectDB():
    global conn
    conn=sqlite3.connect("employes.db")
    global cursor
    cursor=conn.cursor()
    print("connected to database")

def createTable():
    try:
        cmd="CREATE TABLE emps(fname text,lname text,pay integer)"
        cursor.execute(cmd)
        print("emps table is created")
    except Exception as ex:
        print("cannot create table",ex)

def insertEmp(emp):
    try:
        cmd="INSERT INTO emps(fname,lname,pay) VALUES(?,?,?)"
        values=(emp.fname,emp.lname,emp.pay)
        cursor.execute(cmd,values)
        cursor.execute("commit")
        print("employee added to table")
    except Exception as ex:
        print("error in inserting to table",ex)

def readEmps():       
    cursor.execute("SELECT * FROM emps")
    return cursor.fetchall()

def deleteEmp(emp):
    try:
        cursor.execute("DELETE FROM emps WHERE :lname = lname",{'lname':emp.lname})
        cursor.execute('commit')
    except Exception as ex:
        print(ex)

#test code
print("working with sqlite3 database")
#connect to db
connectDB()
#createTable()
#emp1=Employee('sharath','kumar',50000)
#emp2=Employee('uma','shankar',50000)
#insertEmp(emp1)
#insertEmp(emp2)

data=readEmps()
print(data)

print("After deleting")
emp1=Employee('sharath','kumar',50000)
deleteEmp(emp1)

cursor.close()
conn.close()


