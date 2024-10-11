import array as arr

# Important can only store one data type but multiples of it, for mixed used a list

numbers = arr.array('i',[1,2,3,4,5])

print("Original array:", numbers)

# Add an element to the array
numbers.append(6)
print("Array after appending:", numbers)

# Remove from Array
numbers.remove(3)
print("Array after removing:",numbers)

# Accessing a particular elememnt
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("All elements in array:")
for number in numbers:
    print(number)

