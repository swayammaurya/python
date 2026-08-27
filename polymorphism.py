'''
 # Polymorphism in Python (Detailed Explanation)
What is Polymorphism?

Definition (English):
Polymorphism is an Object-Oriented Programming (OOP) concept where one interface (same method or function name) can perform different actions depending on the object.

The word Polymorphism comes from two Greek words:

Poly = Many
Morphism = Forms

Definition (Hindi):
Polymorphism का अर्थ है एक ही method 
या function अलग-अलग objects के लिए 
अलग-अलग तरीके से काम करे।

All animals have the same action (speak()), but the output is different.

           Animal
              |
      -----------------
      |       |       |
     Dog     Cat     Cow
      |       |       |
   Bark()   Meow()   Moo()

Same function → Different behavior.

# Types of Polymorphism in Python (Detailed)

Polymorphism means "One Interface, Many Forms." It allows 
the same method or function name to behave differently
 depending on the object or input.

There are three main types of polymorphism in Python:

1.Compile-Time Polymorphism (Method Overloading - Simulated)
2.Runtime Polymorphism (Method Overriding)
3.Duck Typing (Python-specific Polymorphism)

1. Compile-Time Polymorphism (Method Overloading)
Definition

English:
Method Overloading means creating multiple methods with the
 same name but different parameters.

Hindi:
Method Overloading का अर्थ है कि एक ही method का नाम समान हो, 
लेकिन उसके parameters अलग-अलग हों।

Important: Python does not support true method overloading
 like C++ or Java. If you define two methods with the same 
 name, the last one overwrites the previous ones.
'''
'''
class demo:

    def add(self,a,b=0,c=0):
        print(a+b+c)  
d=demo()
d.add(10)
d.add(20,30)  
d.add(30,20,50) 
'''  
'''  
class Calculator:
    def add(self,*number):
        print(sum(number))
C=Calculator()
C.add(5)
C.add(1,2)
C.add(1,2,3)
C.add(1,2,3,4,5)  '''         

# 2. Runtime Polymorphism (Method Overriding)
'''
Definition

English:
Method Overriding occurs when a child 
class provides its own implementation
 of a method already defined in the parent class.

Hindi:
जब child class, parent class के method
 को अपने तरीके से दोबारा लिखती है, तो उसे Method Overriding कहते हैं।
 '''
'''
class Animal:
    def sound(self):
      print("Animal makes sound")
class Dog(Animal):
   def sound(self):
      print("Dog bark")
class Cat(Animal):
   def sound(self):
      print("Cat meows")

d=Dog()
c=Cat()

d.sound()
c.sound()
'''
'''
class RBI:
    def interest(self):
        print("General Interest")
class SBI(RBI):
    def interest(self):
        print("interest =7%")
class PNB:
    def interest(self):
        print("Intere=8%")

s=SBI()
p=PNB()

s.interest()
p.interest()
'''
'''
# Advantages
Dynamic behavior
Code reuse
Easy to extend programs 

3. Duck Typing
Definition

Python focuses on what an object can do, not what type it is.

If an object has the required method, Python allows it.

Rule:

"If it walks like a duck and quacks like a duck, 
treat it like a duck."
'''
class Dog:
    def speak(self):
        print("Bark")
class Cat:
    def speak(self):
        print("meow")
class Bird:
    def speak(self):
        print("tweet")
def make_sound(animal):
    animal.speak()
d=Dog()
c=Cat()
b=Bird()

make_sound(d)
make_sound(c)
make_sound(b)             

         Feature              | Compile-Time (Overloading)                   | Runtime (Overriding)              | Duck Typing                                     |
| -------------------- | -------------------------------------------- | --------------------------------- | ----------------------------------------------- |
| Definition           | Same method name with different parameters   | Child class changes parent method | Works based on available methods                |
| Supported in Python  | Simulated using default arguments or `*args` | Fully supported                   | Fully supported                                 |
| Inheritance Required | No                                           | Yes                               | No                                              |
| Decision Time        | Compile-time concept (simulated in Python)   | Runtime                           | Runtime                                         |
| Example              | `add(10)`, `add(10,20)`                      | `Dog.sound()`, `Cat.sound()`      | `make_sound()` with any object having `speak()` |
         