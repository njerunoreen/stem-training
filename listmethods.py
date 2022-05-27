#lists
fruits=["apples","orange","banana"]
fruits.append("cherry")
print(fruits)
fruits.remove("cherry")
print(fruits)

my_fruits=fruits.pop(1)
print(fruits)
print(my_fruits)
fruits=["apples","orange","banana"]
fruits_2=["cherry","tomatoes"]
fruits_3=fruits+fruits_2
print(fruits_3)
fruits.extend(fruits_2)
print(fruits)
fruits_2.clear()
print(fruits_2)
fruits_4=("apple","orange","banana")
print(fruits_4)
print(fruits_4[1])
new_lists=list(fruits_4)
new_lists.append("tomato")
fruits_4=tuple(new_lists)

fruits_5={"apples","oranges","oranges","oranges"}
print(fruits_5)
