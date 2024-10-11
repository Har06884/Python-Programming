# 2d array created as a liast due to array module not support multi-dementional arrays

# Using a list (mixed data)
matrix = [
    ["Cat",2,3],
    [4,5,6],
    [7,8,9]
    ]

#using array module
import array as arr
matrixA = [
    arr.array('i',[1,2,3]),
    arr.array('i',[4,5,6]),
    arr.array('i',[7,8,9])
    ]

# Accessing elements
print("Element at row 1, column 2:", matrix[1][2])
print("Element at row 2, column 0:", matrixA[2][0])
matrix[1][1] = 10
print("Modified element os Row 1, Column 1 to 10: ", matrix[1][1])

print("Print all elements in matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
