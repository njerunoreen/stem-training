from __future__ import print_function
from re import sub


num1 = input("Enter first number")
num2 = input("Enter second number")
# re-declare variables

num1 = int(num1)
num2 = int(num2)

# create sum variable

sum = num1+num2
print(sum)
mult = num1*num2
print(mult)

div = num1/num2
print(div)
sub = num1-num2
print(sub)