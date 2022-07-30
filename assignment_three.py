#complex calculator
op=int(input("enter first number"))
op_two=int(input("enter second number"))
op_three=(input("enter operator"))
if "/"== op_three :
    print(op/op_two)
 
elif "*" == op_three :
    print(op*op_two)
 
if  "-" == op_three : 

      print(op-op_two)
elif "+"  == op_three : 
    print(op+op_two)  
# try ,execpt in python to catch errors
try :
    div =10/0    
    value = int (input ( "enter a number :"))
    print(value)

    
    
except ValueError:
    print("invalid number entered")
except ZeroDivisionError :
    print("Divided by zero")    
    
    

    

