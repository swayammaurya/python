'''
Python Dictionary (Complete Detailed Notes - English + Hindi)

Dictionary Python ka ek built-in data type hai jo Key : Value ke form me data store karta hai.

Key → Data ko identify karti hai.
Value → Actual data hota hai.
Ek key ke saath sirf ek hi value hoti hai.
Dictionary ko {} (curly braces) me likhte hain.

1. What is Dictionary?
Definition (English)

A Dictionary is a built-in, mutable mapping data type in
Python that stores data as key-value pairs. Each key is 
unique and maps to a corresponding value

student={
    "name":"rahul",
    "age":20,
    "course":"B.Tech",
    "marks":85
}
print(student)

           Dictionary
               |
--------------------------------
|              |               |
Name          Age           Marks
 |             |               |
Rahul         20             90

employee={
    101:"john",
    102:"Rahul",
    103:"priya"

}
print(employee)
# mutable
student1={
    "number":"Rahul"
}
student1["name"]="Aman"
print(student1)

# Duplicate keys not allowed
student2={
    "name":"rahul",
    "name":"mohan"
}
print(student2)

# DUplicate values allowed
student3={
    "a":"python",  
    "b":"python",
    "c":"python"
}
print(student3)

Allowed Data Types
Keys

Key immutable honi chahiye

str
int
float
tuple
bool

d = {
    1:"One",
    2:"Two",
    True:"Yes",
    (1,2):"Tuple"
}

11. Dictionary Methods (Common)

| Method         | Purpose                           |
| -------------- | --------------------------------- |
| `get(key)`     | Safely value lena                 |
| `keys()`       | Sabhi keys                        |
| `values()`     | Sabhi values                      |
| `items()`      | Key-value pairs                   |
| `update()`     | Dusri dictionary se update        |
| `pop(key)`     | Specific key delete               |
| `popitem()`    | Last inserted item delete         |
| `clear()`      | Sab data hata do                  |
| `copy()`       | Shallow copy                      |
| `setdefault()` | Key na ho to default value insert |



student = {"name": "Rahul", "age": 20}

print(student.keys())
print(student.values())
print(student.items())
 '
# Iterating Through a Dictionary
student={
    "name":"Rahul",
    "age":20,
    "course":"Btech"
}

for key, value in student.items():
    print(key," = ",value)

    
# NESTED DICTIONARY
student={
    "101":{
        
        "name":"Rahul",
        "age":20,
        "course":"Btech"
    },
    "102":{
        "name":"Priya",
        "age":22,
        "course":"M.Tech"
    }
}  
print(student)  

print(student["101"]["name"])
print(student["102"]["age"])

# Dictionary Comprehension

Jaise list comprehension hoti hai, waise hi 
dictionary comprehension bhi hoti hai.

squares={x:x*x for x in range(1,6)}
print(squares)

student = {
    "Name": "Rahul",
    "Age": 20,
    "Branch": "CSE",
    "Marks": 88
}

# Access
print("Name:", student["Name"])

# Add
student["City"] = "Lucknow"

# Update
student["Marks"] = 95

# Delete
student.pop("Age")

# Display
for key, value in student.items():
    print(key, ":", value)

    Definition: Dictionary stores data as key-value pairs.
Syntax: Uses {}.
Keys: Unique and immutable.
Values: Can be any data type and may repeat.
Important Methods: get(), keys(), values(), items(), update(), pop(), clear().
Internal Working: Based on a hash table, giving average O(1) time for search, insertion, and deletion.

Ye notes Python Dictionary ko beginner se advanced level tak cover karte hain aur interview, 
viva, aur exam tino ke liye useful hain.

'''