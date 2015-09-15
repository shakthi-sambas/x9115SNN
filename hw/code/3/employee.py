#!/usr/bin/python3
# In the above I expect the python 3 executable in the given path: If not modify --Shakthi
#  Author: Shakthi Sambasivam
# This is a simple Employee class


class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return "Employee Details :\n" "Name of the Employee: {} \nAge: {}\n ".format(self.name, self.age) 
    
    def __lt__ (self, emp1):
        return self.age < emp1.age
    
    def __gt__ (self, emp1):
        return self.age > emp1.age

def main():
    emp1 = employee("John",55)
    emp2 = employee("Tim",30)
    emp3 = employee("Frank",60)
    
    print (emp1)
    print (emp2)
    print (emp3)
    
    
    list_of_employees = [emp1,emp2,emp3]
    list_of_employees.sort();
    print("Employees sorted based on Age :")
    print(list_of_employees) 
    
    
    

if __name__ == "__main__": main()
