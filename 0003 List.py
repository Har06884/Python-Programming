#########################################################
#                       Part 1: Lists                   #
#########################################################
#                                                       #
# This is the first program that will use a list.       #
#                                                       #
#########################################################

print("Welcome to Python Basic!, This program will discuss Lists")
print()

# Create a list using []
fruit = ["apple","banana","cherry"]

# print the whole list
print(fruit)
# print one item from the list
print(fruit[1])

# add an item
fruit.append("grapes")
print(fruit)

# modify the list
fruit[1] = "oranges"
print(fruit)

# remove from list
#fruit.remove("grapes")
#print(fruit)
# pop from list
#fruit.pop(3)
#print(fruit)
# use del to delete an element
del fruit[3]
print(fruit)
p# clear the list
fruit.clear()
print(fruit)
