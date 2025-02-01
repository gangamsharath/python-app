''''Custom module : app.py'''
import os,sys

name="sharath" #is called a global variable
#create a function
def greet(ename="none"):
    os.system('cls')
    data=[10,20,'sharath'] #private virable
    print(type(data))
    emp=[
        {'eno':101,'ename':'Laxmi'},
        {'eno':102,'ename':'Sharath'}
    ]
    print(type(emp))
    print(emp) 
    first,second=(100,200)
    print(first)

if __name__=='__main__':
    greet("kiran")
    sys.exit()
    
     