


class Person:
    def __init__ (self,name,age,date_of_birth,height,weight):
        self.name=name
        self.age=age
        self.date_of_birth=date_of_birth
        self.height=height
        self.weight=weight
        
    def print_age(self):
        self.age = 2022-self.date_of_birth
        print(f"you are {self.age}years old")
    def print_bmi(self):
        self.bmi = self.height/self.weight
        
        
                  
    
                         
class student(Person):
    def __init__ (self,name,age,date_of_birth,height,weight,stream,favourite_subject):
        super().__init__(name,age,date_of_birth,height,weight)
        self.stream=stream
        self.favourite_subject=favourite_subject
    def print_stream(self):
        print(f"you are in stream{self.stream}")
    def print_ (self):
        print(self.favourite_subject)   
        
class teacher(Person):
    def __init__(self, name, age, date_of_birth, height, weight ,subject_teaching,salary):
        super().__init__(name, age, date_of_birth, height, weight)
        self.subject_teaching = subject_teaching
        self.salary = salary
    def subject_teaching(self):
        print(self.subject_teaching) 
    def salary(self):
        print(self.salary)       
p1= Person(name="mwende",age=22,date_of_birth=15,height=5,weight=58)
p2=Person(name="wakio",age=15,date_of_birth=12,height=4,weight=44,) 
p3=Person(name="wekendi",age=14,date_of_birth=11,height=3,weight=40,)

print(p1.name,p1.age,p1.date_of_birth,p1.height,p1.weight 
print(p2.name,p2.age,p2.date_of_birth,p2.height,p2.weight) 
print(p3.name,p3.age,p3.date_of_birth,p3.height,p3.weight) 
               
            

    
        