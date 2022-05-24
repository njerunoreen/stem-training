
from re import X
from unicodedata import name

from pkg_resources import safe_name


name = "noreen"

#multiple line strings
msg =  """QRS3X CONFIRMED YOU HAVE RECEIVED FROM JANET MUENI SAFARICOM CARES FOR YOU"""
print(msg)

city = "nairobi"
# .upper() to convert to upper case
print(city.upper())
uni = "JKUAT"

print(uni.lower())

fruit = "watermellon"

print(fruit[:2])
print(fruit[5:])
print(fruit[-1:])

#strip removes spaces between word
f_name ="  njeru"
print (f_name.strip())
s_name = "noreen"
full_name = f_name +s_name
print(full_name)

city = "mombasa"

print(len(city))

word ="abracadabra" 
print(len(word))

#int - > string
x = 100 
y = 3.14
z = 1
print(str(X))
print(str(y))
