#oop
#defining a class and its attributes
#method overriding
#class methods(functions belonging to a class)





class Dog:
    def __init__ (self, no_of_eyes ,color ,no_of_legs ,nose):
        self.no_of_eyes = no_of_eyes
        self.color = color
        self.no_of_legs = no_of_legs
        self.nose = nose
        
    def barking (self):
        print("Woof woof!")
        
    def wagging_tail(self) :
        print("walking")
            
German_shephered= Dog(no_of_eyes=2,color='grey',no_of_legs=4 ,nose = 'black')
doger = Dog(no_of_eyes=1 , color='white' , nose= 'black' ,no_of_legs=4)
dobberman =Dog(2, 'brown',4,'black')



print(German_shephered.color,German_shephered.no_of_eyes)
print(doger.no_of_eyes,doger.color)
print(dobberman.color, dobberman.no_of_eyes)
dobberman.color = "dark brown"
print(dobberman.color)
print(dobberman.no_of_eyes)
dobberman.barking()
