#🔹 1. Function :-
'''
In Python, a function is a block of code that performs a specific task and can be reused whenever needed.

🔹 1. Function Definition

You create a function using the (def) keyword:
 Ex
def function_name():
    print("Hello, this is a function")

🔹2. Calling a Function

To run the function, just write its name with parentheses:

function_name()

🔹 3. Function with Parameters

You can pass values (inputs) to a function
'''
'''
def greed(name):
     print("hello",name)
greed("swayam") '''
'''
🔹 4. Function with Return Value

A function can return a value using return:
def add(a,b):
    return a+b
c=add(5,6)
print("add a+b =",c)
'''
'''
🔹 5. Types of Functions

Built-in functions → already in Python
Example: print(), len(), type()
User-defined functions → created by you
Example: add(), greet()'''

'''
#Q1. Write a program using functions to find greatest of three numbers.
 
def greatest(a,b,c):
    if(a>b and a>c):
       print("a is greatest")
    elif(b>a and c>b):
       print("b is greatest")
    else:
       print("c is greatest")
a=int(input("enter the a =")) 
b=int(input("enter the b =")) 
c=int(input("enter the c =")) 
greatest(a,b,c)'''

'''
#Q2. Write a python program using function to convert Celsius to Fahrenheit.

def ce_to_fa(celsius):
    fahrenheit=(celsius*(9/5)) + 32
    print("convert celsius to fahrenheit=",fahrenheit)
c=int(input("enter the value in celsius="))
f=ce_to_fa(c)
print(f)

# simple intrence
def sim_in(t,p,r):
    simple=(t*r*p)/100
    print("simple intrance",simple)
t=int(input("enter the time="))  
r=int(input("enter the rate="))  
p=int(input("enter the principal="))    
sim_in(t,p,r)'''


