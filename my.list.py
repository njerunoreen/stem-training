my_list=[1,2,3,4,5]
for element in my_list :
       print(element)
other_list=[]  
other_list.append(element) 
print(other_list)
my_list=[1,2,3,4,5]
other_list=[element for element in my_list]  
print(other_list)
for element in my_list :
    if element % 2 ==0:
        other_list.append(element)
print(other_list)      
my_list=[1,2,3,4,5]
other_list=[element for element in my_list if element %2==0]
print(other_list)

def add (a,b) :
   return a+b 

result = add (4,6)
print(result)
def mean (a,b) :
   return (a+b) / 2   
result = mean (4,6)
print(result)
