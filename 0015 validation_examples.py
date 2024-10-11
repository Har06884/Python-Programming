'''def get_number():
    #create a loop for validation
    while True:
        user_input = input("Please enter a number: ")
        #if statments based upon validation check
        if user_input.isdigit(): #.isdigit() only accepts whole non-negative numbers
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid number.")

#function as they return a value need a variable to store that value in as this can be used
#elsewhere in the program. As the developer you deciced if a function/procedure is needed.
number = get_number()'''

#try-except-finally
#a better validation method

def get_number2():
    while True:
        user_input = input("Please enter a number: ")
        # try attempts the code (in this case to convert a user input to an integer)
        try:
            number = int(user_input)
            return number
        # Catches a ValueError if an the input is invlaiud and prompts again
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        # Runs regardless of the exception occuring, this indicates the input process.
        # doesn't always need to be added
        finally:
            print("Attempted to process input")

number = get_number2()
print(f"You entered: {number}")
