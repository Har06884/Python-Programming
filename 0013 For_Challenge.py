while True:
    number =(input("Please enter a number above 10: "))

    if number.isdigit() and int(number) > 10:
        number=int(number)
        print(f"Your number is {number}!")
        break
    else:
        print(f"Your number {number} is incorrect!")

for i in range (1, number+1):
    print(f"(Number: {i}, Eigth Power: {i ** 8}")


                
