


class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print(f"my name is {self.name} and my age is {self.age}") 
        
        
p1 = Person("mwende",18)        
p1.details()

class Employee(Person):     
    def __init__(self, name, age ,salary):
        super().__init__(name, age)
        self.salary = salary
        
    def birthday (self):
        self.age=self.age+1
        print(f"Happy birthday,you are now {self.age} years old") 
           
p2 = Employee("mwende",18 ,2500) 
p2.details()    

    
        