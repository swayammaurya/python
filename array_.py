'''📌 Definition of Array in Python (Simple English)

English:-An array is a data(same datatype) structure that stores multiple elements in a single variable, 
and each element can be accessed using an index (position).

Hindi:-Array ek data structure hota hai jisme hum multiple values ko ek hi variable me store karte hain,
 aur un values ko index number (position) ke through access karte hain.
🧠 Key Points
1.Elements are stored in an ordered manner
2.Each element has an index starting from 0
3.Arrays are mainly used to store similar types of data
4.In Python, we usually use lists as arrays
🔹 Example
numbers = [10, 20, 30, 40]
numbers[0] = 10
numbers[1] = 20
✅ One-Line Definition (for exam)

“An array is a collection of elements stored in a single variable, which can be accessed using index positions.”'''
'''
1️⃣ Creating an Array (List) in Python
# Creating a list of numbers
numbers = [10, 20, 30, 40, 50]

print(numbers)

Output:

[10, 20, 30, 40, 50]'''
'''
2️⃣ Accessing Elements

Index starts from 0.

numbers = [10, 20, 30, 40, 50]

print(numbers[0])  # First element
print(numbers[2])  # Third element

Output:

10
30'''
'''
#3️⃣ Adding Elements
numbers = [10, 20, 30]

numbers.append(40)
print(numbers)'''

'''
 4️⃣Changing Elements
numbers = [10, 20, 30, 40, 50]

numbers[1] = 25
print(numbers)'''
'''
# 5️⃣Removing Elements
numbers = [10, 20, 30, 40]

numbers.remove(20)   # Remove value
print(numbers)

numbers.pop()        # Remove last element
print(numbers)'''

#6️⃣ Looping Through an Array
'''
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)'''

#7️⃣ Length of an Array
'''
numbers = [10, 20, 30, 40,50]

print(len(numbers))'''

# 8️⃣ Real Python Array (Using array Module)

# Python also has a special array module (stores same type only).
'''
Syntax:-
import array

arr = array.array(typecode, [elements])
🔹 Typecodes (Important)
Typecode	Meaning

'i'	        Integer
'f'	        Float
'd'      	Double (float)
'''
'''
import array

numbers = array.array('i', [1, 2, 3, 4])

print(numbers)'''

# 'i' means integer type.
# All values must be integers.

'''
# 2D Array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element
print(matrix[0][1])   # 2
print(matrix[2][2])   # 9

# Loop through matrix
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
'''
'''
#3D array
arr = [
    [
        [1,5, 2],
        [3,7, 4],
        [1,2, 3]
    ],
    [
        [5,6, 6],
        [7,8, 8],
        [9,8, 5]
    ]
]

# Print all elements
for block in arr:
    for row in block:
        for element in row:
            print(element, end=" ")
        print()
    print() '''
'''
arr = []

for i in range(1):          # block
    block = []
    for j in range(1):      # row
        row = []
        for k in range(5):  # 5 elements
            row.append(k + 1)
        block.append(row)
    arr.append(block)

print(arr)'''

'''
#3d array
arr = []
# number of blocks
for i in range(2):
    print("Block", i)
    block = []
    
    # rows
    for j in range(2):
        row = []

        # columns
        for k in range(2):
            num = int(input("Enter element: "))
            row.append(num)
        
        block.append(row)
    
    arr.append(block)

print("3D Array is:")
print(arr)'''
'''
# First 3D array
arr1 = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Second 3D array
arr2 = [
    [[1, 1], [1, 1]],
    [[2, 2], [2, 2]]
]

# Result array
result = []

for i in range(2):  # block
    block = []
    for j in range(2):  # row
        row = []
        for k in range(2):  # column
            sum_val = arr1[i][j][k] + arr2[i][j][k]
            row.append(sum_val)
        block.append(row)
    result.append(block)

print("Sum of 3D arrays:")
print(result)
'''

