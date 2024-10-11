# This is an output statment.
print("Hello World")

# This uses the input function to ask the user to add data
yourName = input("What is your name? ")
#print(yourName)

# This is a string concatenation
print("Hello " + yourName + ", nice to meet you")

# Input statment with a declared data type for integer
age = int(input("What is your age? "))
# you need to convert the data type from one to another this example int to str
print("Your are " + str(age) + " years old")
# This allows you to use mix variable data types without converting, but isn't a concatenation
print(yourName , "is" , age , "years old!")



