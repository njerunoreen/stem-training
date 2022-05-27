f_number =int(input("enter first number"))
s_number =int(input("enter second number"))

sum_of_numbers = f_number + s_number
print("the sum of the two numbers is ="+str(sum_of_numbers))

mult_of_numbers = f_number * s_number
print("the mult of the two numbers is ="+str(mult_of_numbers))

div_of_numbers = f_number / s_number
print("the div of the two numbers is ="+str(div_of_numbers))

sub_of_numbers = f_number - s_number
print("the sub of the two numbers is ="+str(sub_of_numbers))
# try ,execpt in python to catch errors
try :
    div =10/0    
    value = int (input ( "enter a number :"))
    print(value)

    
    
except ValueError:
    print("invalid number entered")
except ZeroDivisionError :
    print("Divided by zero")     


       