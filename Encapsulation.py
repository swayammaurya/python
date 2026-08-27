'''
# Encapsulation in Python (Encapsulation = Data Hiding) 🐍
Definition


English:
Encapsulation is the process of wrapping data 
(variables) and methods (functions) into a single
 unit (class) and restricting direct access to the data.

Hindi:
Encapsulation का मतलब है Data (variables) और
 Functions (methods) को एक ही Class के अंदर रखना और 
 Data को सीधे (directly) access होने से बचाना।
 
 # Real-Life Example
ATM Machine
ATM में आपका Balance hidden रहता है।
आप balance को सीधे change नहीं कर सकते।
Balance बदलने के लिए केवल:
Deposit()
Withdraw()
CheckBalance()

methods का उपयोग करते हैं।

यही Encapsulation है।

# Access Specifiers in Python

Python में 3 प्रकार के access levels होते हैं:

| Access Type | Symbol        | Accessible From                            |
| ----------- | ------------- | ------------------------------------------ |
| Public      | `self.name`   | Everywhere                                 |
| Protected   | `self._name`  | Class and subclass (by convention)         |
| Private     | `self.__name` | Inside the same class only (name mangling) |


# 1. Public Member

Public members को कहीं से भी access किया जा सकता है।
 
class student:
    def __init__(self):
        self.name="swayam"
s=student()
print(s.name) '''

'''# 2. Protected Member (_)

Protected member के पहले एक underscore (_) लगाया जाता है।

यह convention है कि इसे class और child class में उपयोग करें।

Example:-
'''
'''
class student:
    def __init__(self):
        self._marks=90
class result(student):
    def display(self):
        print(self._marks)

r=result()
r.display()    
''' 
'''   
 # 3. Private Member (__)

Private member के पहले double underscore (__) लगाया जाता है।

इसे class के बाहर सीधे access नहीं कर सकते।

Example
'''
'''
class student:
    def __init__(self):
        self.__salary=50000

obj=student()
print(obj.__salary) '''

# fixed
class employee:
     def __init__(self):
          self.__salary=50000
     def  show(self):
          print("salary",self.__salary)

e=employee()
e.show()              
  
  