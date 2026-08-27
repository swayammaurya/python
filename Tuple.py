'''# Tuple in Python (Complete Detailed Explanation)
# Q:What is a Tuple?
# Definition (English)

A tuple is an ordered, immutable (unchangeable) collection of
elements in Python. It can store multiple items of different 
data types and allows duplicate values. Tuples are created using parentheses ().

# Definition (Hindi)

Tuple Python का एक ordered (क्रमबद्ध) और immutable
(जिसे बनाने के बाद बदला नहीं जा सकता) data structure है। 
इसमें अलग-अलग data types की values store की जा सकती हैं 
और duplicate values भी allowed होती हैं। Tuple को parentheses () के अंदर लिखा जाता है।

| Feature    | List   | Tuple                        |
| ---------- | ------ | ---------------------------- |
| Symbol     | `[]`   | `()`                         |
| Mutable    | ✅ Yes  | ❌ No                         |
| Ordered    | ✅ Yes  | ✅ Yes                        |
| Duplicates | ✅ Yes  | ✅ Yes                        |
| Speed      | Slower | Faster                       |
| Memory     | More   | Less                         |
| Methods    | Many   | Only `count()` and `index()` |

tuple_name = (item1, item2, item3)

number=(10,20,30,40,50)
print(number)

# multiple Data Types
data=(10,"apple",3.14,True)
print(data)

# Nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)

# note: A tuple with a single element requires a trailing comma to
#  distinguish it from a regular parentheses expression. For example, (5,) 
# is a tuple with one element, while (5) is just the number 5.not a tuple.
t = (5)
print(type(t))

t = (5,)
print(type(t))

# Accessing Elements

#Tuple indexing exactly list की तरह होती है।


Each element has an index.

fruits=('banana','apple','mango')
print(fruits)

data=(10,'apple',3.14,True )
print(data)

Index:     0        1        2        3

List =   ("Apple","Banana","Mango","Orange")

#Negative Index

          -4      -3      -2      -1

          '''
'''
data=('swayam',3,34.5,True)
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

# tuple[start:stop:step]

tuple1=(10,20,30,40,50,)
print(tuple1[:3])
print(tuple1[3:])

Tuple Methods

Tuple में केवल 2 built-in methods हैं।

Method	Description
count()	Count occurrences
index()	Return index

number=(10,20,30,40,50,)
print(number.count(20))

print(number.index(30))

# len
print(len(number))

# min
print(min(number))

# max
print(max(number))

# sum
print(sum(number))

#Loop through a tuple

data=(10,20,30,40)
for i in data:
    print(i)

i=0
while i<len(data):
    print(data[i])
    i+=1    

# Tuple Concatenation
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)

t=(1,2,3)

a,b,c=t
print(a)
print(b)
print(c)

a=10
b=20
a,b=b,a
print(a,b)

#loop for tuple
t2=(1,2,3,4,5)
for t2 in t2:
    print(t2)
    '''
#Tuple repetition
t3=((1,2)*4)
print(t3)

# convert list to Tuole
t4=(1,2,3)
l=list(t4)
print(l)

l=[1,2,3,5]
print(tuple(l))