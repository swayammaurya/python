'''Object-Oriented Programming (OOP) in Python (Detailed)

Definition (English)

Object-Oriented Programming (OOP) is a programming paradigm that 
organizes software using objects instead of functions and logic.
Objects contain both data (attributes) and methods (functions).

Definition (Hindi)

Object-Oriented Programming (OOP) ek programming technique hai 
jisme program ko objects ke form me banaya jata hai. Har object
ke paas data (variables) aur functions (methods) hote hain.

Car
│
├── Data
│      Color
│      Brand
│      Speed
│
└── Functions
       Start()
       Stop()
       Brake()

Advantages of OOP

Code Reusability
Easy Maintenance
Security
Modularity
Real-life Modeling
Easy Debugging
Faster Development

# Four Pillars of OOP

              OOP
               │
 ┌─────────────┼─────────────┐
 │             │             │
Encapsulation Inheritance Polymorphism
               │
         Abstraction


These four concepts are the backbone of OOP. 

Important     Terminologies
Term	       Meaning
Class	       Blueprint
Object	       Real instance
Attribute	   Variable
Method	       Function
Constructor	   Special function

1. Class
Definition

A Class is a blueprint for creating objects.

Hindi:

Class ek naksha (Blueprint) hota hai jisse objects bante hain.

Example

Blueprint

House Plan
      ↓
Many Houses


Python Syntax

class Student:
    pass
    

2. Object

Definition

Object is an instance of a class.

Hindi

Object class ka real example hota hai.

Example

class Student:
    pass

s1 = Student()
s2 = Student() 

Student → Class

s1 → Object
s2 → Object
         '''
'''
# Creating Attributes

class Student:
    pass
s1=Student() 
s1.name="swayam"
s1.age=20
print(s1.name)
print(s1.age)
'''
'''
class bank:
     name="swayam maurya"
     acc_no=2532916522
     IFC_no=2845485
     branch="hohata"
     age=20
c1=bank() #object
print(c1.name)
print(c1.acc_no)
print(c1.IFC_no)  
print(c1.branch)
print(c1.age) 

# Constructor

Constructor in Python (Detailed Explanation)
What is a Constructor?

Definition (English):
 A constructor is a special method in Python that is
 automatically called when an object of a class is 
 created. It is mainly used to initialize the object's data (attributes).

Definition (Hindi):
Constructor Python का एक special method है जो object बनते ही 
automatically execute हो जाता है। इसका उपयोग object की variables 
(attributes) को initial values देने के लिए किया जाता है।

Constructor automatically object banate time call hota hai.

Syntax

class Student:
    def study(self):
        print("i am astudent")
si=Student()     


# Instance Variable

Har object ka alag variable.

Example

# Methods



Method class ke andar likha function hota hai.

class Student:

    def study(self):
        print("Studying")

class Student:
    def __init__(self):
        print("Constructor Called")

s1 = Student()

Types of Constructor in Python

Python में मुख्य रूप से 2 प्रकार के constructors होते हैं।

1 Default Constructor # जिस constructor में कोई parameter नहीं होता।
2 Parameterized Constructor
'''
'''
# Default Constructor
class student:
    def __init__(self):
        self.brand="toyota"
c=student()    
print(c.brand)
'''
'''
# prameterized Constructor
class Car:
    def __init__(self, color, brand, speed):
        self.color = color
        self.brand = brand
        self.speed = speed

    def start(self):
        print(f"The {self.color} {self.brand} is starting.")

    def stop(self):
        print(f"The {self.color} {self.brand} is stopping.")

    def brake(self):
        print(f"The {self.color} {self.brand} is braking.")
c1=Car("Red", "Toyota", 120)  
c1.start()
c1.stop()
c1.brake()      
'''

'''
class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

c = Car("Toyota","Fortuner")

print(c.brand)
print(c.model)
'''
'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print("Employee:",self.name)
        print("Salary:",self.salary)  
e=Employee("Amit",5000)
e.show() 

'''

'''
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student("Rahul", 101)
s1.display() 
'''
'''
  # Memory Diagram
            Student Class
        ---------------------
        | __init__()        |
        | display()         |
        ---------------------
                 |
                 |
          Object s1
        -----------------
        | name = Rahul   |
        | roll = 101     |
        -----------------
        '''
'''
# construvtor in inheritance
class Animal:
    def __init__(self):
        print('Animal constructor')
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")
d=Dog() 
'''   

# area of Rectangle
'''
class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        return self.length*self.breath
r=Rectangle(10,5)
print("Area=",r.area()) 
'''
'''
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
    def display(self):
        print(self.name)
        print(self.balance)
b=Bank("Rahul",1000)
b.deposit(500)        
b.display()  
'''
'''
# Advantages of Constructor

Object creation के साथ initialization automatically हो जाता है।
Code reusable और clean रहता है।
हर object की initial state आसानी से set की जा सकती है।
Errors कम होते हैं क्योंकि required values शुरुआत में ही मिल जाती हैं।
OOP principles को follow करना आसान होता है।

# Important Interview/Exam Points

__init__() Python का constructor है।
Constructor object create होते ही automatically call होता है।
self current object को represent करता है।
Constructor का मुख्य उद्देश्य object की attributes initialize करना है।
Python में मुख्यतः Default Constructor और Parameterized Constructor का उपयोग किया जाता है।
Python constructor overloading को directly support नहीं करता; इसे default arguments (x=None) या variable-length arguments (*args, **kwargs) से handle किया जाता है।
Parent class के constructor को call करने के लिए super().__init__() का उपयोग किया जाता है।

# Inheritance in Python (Detailed)
What is Inheritance?

Definition (English):
Inheritance is an Object-Oriented Programming (OOP) 
feature that allows one class (child class) to acquire 
the properties and methods of another class (parent class).

Definition (Hindi):
Inheritance एक ऐसा OOP concept है जिसमें एक Child Class 
दूसरी Parent Class के variables और methods को inherit (प्राप्त) कर लेती है।

Syntax:

class Parent:
    # Parent class code

class Child(Parent):
    # Child class code

    Why Use Inheritance?
1.Code Reusability :-        एक ही code को बार-बार लिखने की जरूरत नहीं।
2.Easy Maintenance :-          Code को manage करना आसान होता है।
3.Extensibility :-             Existing class में नए features जोड़ सकते हैं।
4.Hierarchical Relationship :- Parent-Child relationship बनती है। 

Real Life Example
            Animal
           /      \
        Dog       Cat
Animal → Parent Class
Dog → Child Class
Cat → Child Class

Animal की सभी properties Dog और Cat में आ जाती हैं।

Types of Inheritance in Python

Python में मुख्यतः 5 प्रकार की Inheritance होती हैं।

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
    ''' 
# Example 1 : Single Inheritance
'''       
class Animal:
    def __init__(self):
        print("Animal costrutor")
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
d=Dog()
d.eat()
d.bark() 
'''
# 2 multipal inheritance
'''

class Animal:

    def eat(self):
        print("Animal eats")


class Mammal(Animal):

    def walk(self):
        print("Mammal walks")


class Dog(Mammal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.walk()
d.bark()
'''
# 3 multilevel inheritance
'''
class animal:
    def eat(self):
        print("Animal eat")

class cat:
    def voice1(self):
        print("mow mow ladale") 
class dog:
    def voice2(self):
        print("dog bark")
class horse:
    def voice3(self):
        print("hourse HIN HIN")
class pet(animal,cat,dog,horse):
    pass        
d=pet()
d.eat()
d.voice1()                                                      
d.voice2()
d.voice3()
'''
# 4 Hierarchical inheritance
'''
class animal:
    def eat(self):
        print("animal")

class Dog(animal):
    def bark(self):
        print("Dog bark")
class cat(animal):
    def meow(self):
        print("cat meow") 
d=Dog()
c=cat()

d.eat()
d.bark()

c.eat()
c.meow()
'''
# 5 Hybrid Inheritance :-two or more types of inheritance
'''
# Diagram (Multiple + Multilevel Hybrid)
        Animal
       /      \
    Mammal    Bird
       \      /
          Bat          '''
'''
class animal:
    def eat(self):
        print("animal")
class mammal(animal):
    def walk(self):
        print("ammmal walk")
class bird(animal):
    def fly(self):
        print("Bird flies")
class bat(mammal,bird):
    def sleep(self):
        print("bat sleep")    
b=bat()

b.eat()
b.walk()
b.fly()
b.sleep()
'''