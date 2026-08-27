'''
# Python List (Detailed Explanation)
What is a List?

Definition (English):
A list in Python is an ordered, mutable (changeable),
and indexed collection that can store multiple items of different data types.

Definition (Hindi):
List Python ka ek data structure hai jo multiple values
ko ek hi variable mein store karta hai. List ordered,
changeable (mutable) aur indexed hoti hai.
Ex

list_name=[item1,ilem2,item3]

# Characteristics of List

| Property            | Description                                    |
| ------------------- | ---------------------------------------------- |
| Ordered             | Elements have a fixed order.                   |
| Mutable             | Elements can be changed after creation.        |
| Indexed             | Starts from index 0.                           |
| Allows Duplicates   | Duplicate values are allowed.                  |
| Multiple Data Types | Can store int, float, string, bool, list, etc. |


# Indexing

Each element has an index.

fruits=['banana','apple','mango']
print(fruits)

data=[10,'apple',3.14,True ]
print(data)

Index:     0        1        2        3

List =   ["Apple","Banana","Mango","Orange"]

Negative Index

          -4      -3      -2      -1

          

data=['swayam',3,34.5,True]
print(data[0])
print(data[1])
print(data[2])
print(data[3])

#Negative index

print(data[-1])
print(data[-2])
print(data[-3])
print(data[-4])

# List Slicing

list[start:stop:step]
'''
'''
number=[10,20,30,40,50,60]
print(number[0:3])

print(number[2:]) # From Index 2 to End

print(number[:4]) # From Beginning to Index 4

# nested list
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(matrix)

# append (adds one element at the end of the list)
fruits=['banana','apple']
fruits.append('mango')
print(fruits)

# insert (adds one element at the specified index)
fruits=['banana','mango','orange']
fruits.insert(2,'apple')
print(fruits)

# extend (adds multiple elelments at the end of the list)
fruits=['banana','mango','orange']
fruits.extend(['apple','grapes'])
print(fruits)

# remove( Removes by value)
fruits=['banana','mango','orange']
fruits.remove('mango')
print(fruits)

# pop (removes by index)
fruits=['banana','mango','orange']
fruits.pop(2)
print(fruits)

# del(removes by index
numbers=[10,20,30,40,50]
del numbers[2]
print(numbers)

#clrar(removes all elements from the list
numbers=[10,20,30,40]
numbers.clear()
print(numbers)

#index
numbers=[10,20 ,30,40]
print(numbers.index(30))

# count
numbers=[10,20,30,40]
print(numbers.count(20))

#sort
numbers=[10,20,30,40]
numbers.sort()
print(numbers)


numbers=[10,20,30,40]
numbers.sort(reverse=True)
print(numbers)

#reverse
numbers=[10,20,30,40]
numbers.reverse()
print(numbers)

#copy
list1=[1,2,3,4]
list2=list1.copy()
print(list2)

#length
numbers=[10,20,30,40]
print(len(numbers))

# max
numbers=[10,45,74,23]
print(max(numbers))
print(min(numbers))

#Looping through a list

fruits=['Apple',"Banana" ,"mango"]
for fuit in fruits:
    print(fruits) 

list1=[10,20,30,40]
for i in range(len(list1)):
    print(list1[i])

while i < len(list1):
    print(list1[i])
    i+=1

# List Comprehension

# A concise way to create lists.
square=[i**2 for i in range(1,6)]
print(square)

even=[i for i in range(20) if i%2==0]
print(even)


 # Advantages of Lists
Easy to create and use.
Stores multiple values in one variable.
Allows different data types.
Supports indexing and slicing.
Many built-in methods.
Dynamic size (can grow or shrink).


 # Disadvantages of Lists

Uses more memory than some other data structures.
Searching in a large list can be slower.
Inserting or deleting elements in the middle may be less efficient.

# Interview / Exam Questions 

What is a list in Python?
Why is a list called mutable?
Differentiate between append() and extend().
Explain positive and negative indexing.
What is list slicing?
Difference between remove() and pop().
Explain list comprehension with an example.
How do sort() and sorted() differ?
What is the difference between a shallow copy (copy()) and simple assignment (=)?
Explain nested lists with an example.
# Summary
List is an ordered, mutable, and dynamic collection in Python.
It is created using square brackets [].
It supports indexing, slicing, updating, inserting, deleting, sorting, and iteration.
Lists can store duplicate values and different data types.
They are one of the most important and frequently used data structures in Python.
'''