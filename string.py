'''
#String in Python (Detailed Explanation)
Definition (Exam Definition)

A string in Python is a sequence of characters enclosed within single 
quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
Strings are used to store text such as names, messages, addresses, and sentences

str1='swayam'         #single quotes
str2="maurya"         #double quotes
str3=""" B.tech"""    #triple quotes
print(str1,str2,str3)    

 # Accessing Characters
String = "PYTHON"

Index:

Positive Index
 0   1   2   3   4   5
 P   Y   T   H   O   N

Positive Index
word="python"
print(word[2])
print(word[4])
print(word[5])


Negative Index:
-6 -5 -4 -3 -2 -1
 P  Y  T  H  O  N

Negative Index:
print(word[-1]) # you find the last character
print(word[-3])
print(word[-2]) 

# String Slicing

Syntax

string[start : stop : step]


text="python programning"
print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])
 
 # Reverse a String

text='python programing'
print(text[::-1])
 
 # string Length

text="python"
print(len(text))

# sting Repetition
str='swayam'
print(str*12) 

# sting Concatenation
first="swayam"
second="maurya"
print(first +" "+second)

#Membership Operators

Check whether a word exists inside a string. 

text='python programing'

print('python' in text)
print('java' in text) 


#Looping throw a string 
text="swayam"
for i in text:
    print(i)
'''
'''
#upper
text='swayam'
print(text.upper())

#lower
str="MAURYA"
print(str.lower())

#capitalize :- first character is capital
str1='python'
print(str1.capitalize())

#title:- start with a capital letter.
str2='mohan is good boy'
print(str2.title())

#replace
str3='python is berst program'
print(str3.replace("python","java"))

#split
str4='mongo banana orange'
print(str4.split())

#find
str5="python"
print(str5.find("t"))

#count
str6="banana"
print(str6.count("a"))

#startswith and endswith
str7='python is good language'
print(str7.startswith("python"))
print(str7.endswith("language"))
# String Formatting
#Using f-string (Recommended)
name="swayam"
age=20
print(f"my name is {name} and i am {age} year old ")

#Advantages of Strings
Store text data efficiently.
Easy to manipulate using built-in methods.
Support indexing and slicing.
Immutable, making them safer to use.
Widely used in file handling, web development, databases, and user input.


#Applications of Strings
Storing names and addresses.
Processing user input.
Password validation.
File handling.
Data analysis.
Web development.
Chat applications.
Email processing.''' 
