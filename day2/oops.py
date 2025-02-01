#oops module

#class Employee() #by default its object
class Employee(object):
     #constructor
     def __init__(self,empno,ename,salary):
          self.name=ename #instance variables/properties
          self.eno=empno
          self.pay=salary
#          self.bonus=50000  #public
          self.__bonus=50000  #private instance property

     def showDetails(self):
         print('Empno',self.eno)
         print('Emp name',self.name)
         print('Salary',self.pay)
         print('total amt', self.pay+self.bonus)
     
if __name__=='__main__':     
  e1=Employee(101,'sharath',50000000)
  e1.showDetails()
  e2=Employee(102,'radhya',50000000)
  e2.showDetails()
  print(e1.bonus)