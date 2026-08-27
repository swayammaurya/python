

#chapter 1

#print("swayam")

'''
a=10
b=20
print (a+b)'''

#chapter 2:
'''
a=10
s=type(a)#int
print(s)
b="swayam"
type(b)#str
c='31'
type(c)#float '''
#Q.1
'''
a=int(input('enter the number a='))
b=int(input('enter the number b='))
c=a+b
print('sum=',c)'''


#Q.2
'''
a=int(input('enter the number a='))
b=int(input('enter the number b='))
c=a%b
print('remainder=',c)'''

#Q.3

'''
a=10
type(a)#int
b="swayam"
type(b)#str
c='31'
type(c)#str '''

#Q.5
'''
a=int(input('enter the number a='))
b=int(input('enter the number b='))
c=(a+b)/2
print('avarage=',c)'''

#Q.6
'''
a=int(input('enter the number a='))
c=a**2
print('square=',c)
'''
# binary 
'''
a=0b100  #4
print(type(a))
print(a)
b=0B1111
print(b)# 15
        '''    
# octal
'''
a=0o123
print(type(a))
print(a)'''

#hexademial
'''
a=0xAFBC
print(type(a))
print(a)'''


# direct
'''
print(hex(21))
print(bin(15))
print(oct(154))'''

#complex number
'''a=23+65j
print(type(a))

b=0b1111+5j
print(type(b))

c=52.6+5j
print(type(c))
            
d=0b1111+01111j # wrong
print(type(d))

b=0b1111+5j
print(cvar.imag)'''

#scape characer
'''
\n= next line
\t=gap
\\
\'

'''
#chapter (3) string
'''
 :-string is a data type in python.
 :-string is a sequence of characters enclosed in quotes.
 :-The index in a string from start from 0 to (length-1) in python .
   in order to slice a string ,we use the follwoing syntex.
  
 :-we can primarily wrte a string in these three ways.
 a='swayam'
 a="swayam"
 a=""swayam""
 
 name="swayam", s w a y a m
       012345  (-6-5-4-3-2-1) 
      ''' '''
       name="swayam"
      nameshort=name[1:3]
      print(nameshort)
      print(name[2])#a
      print(name[3])#y
      print(name[4])#a
      print(name[0:])#swayam
      print(name[:5])#swayam
     print(name[1:5:2])#wy
      name[start:end:difference] 
    '''
     '''
     #string function
     #length function
name="swayam"
     
print(len(name))#6
     
     #string.endswith("ayam")
print(name.endswith("yam"))#true
     
     #string.count("a")
count=name.count("a")
print(count)#2
                    
     #string.replace
replace=name.replace("s","p")
print(replace)
              

'''     
                    
   #loops
   
'''
i = 0
while (i < 6):
    print(i)
    i += 1
    '''

'''   
l=[1,"swayam","maurya","mohan"]
j=0
while(j<len(l)):
     print(l[j])
     j+=1
'''
'''
#for loops
    for i in range(7):
    print("i am swayam")
    
    l=[1,3,4,"swayam","maurya",6]
    for i in range(6):
    print(l[i])
  #for loop with lists
  
    l=[3,5,34,66,34]
    for i in l:
        print(i)
  #for loop with string
  
     l="swayam"
     for i in l:
         print(i)
  #for loop with tuple
  
     t=(4,56,7,3,6)
     for i in t:
         print(i)
  # table
  for i in range(5,100,5)
  print(i)
  # range(start,end,diffrence)

  # for loop with else
  l=[2,34,6]
  for i in l:
   print(i)
  else:
      print("done")
      
  #for loop with break 
  
  for i in range(5,100,5):
 if i==15:
 break
 print(i)

# continue

for i in range(5):
    if i==2:
        continue
    print(i)

l = [3,5,6,7]
for i in l:
    pass   # ये कुछ नहीं करेगा

l = [5,1,8,6]
for i in l:
    print(i)
'''
 #conditional
 
 
'''#four greatest number
n1=int(input("enter the fiest number 1: "))
n2=int(input("enter the fiest number 2: "))
n3=int(input("enter the fiest number 3: "))
n4=int(input("enter the fiest number 4: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("n1 is greatest number")
elif (n2>n1 and n2>n3 and n2>n4):
    print("n2 is greatest number")   
elif (n3>n2 and n3>n1 and n3>n4):
    print("n3 is greatest number")   
elif(n4>n2 and n4>n3 and n4>n1):
    print("n4 is greatest number") '''

'''
#pass and fail in exam
s1=int(input("s1 subject marks: "))  
s2=int(input("s2 subject marks: "))  
s3=int(input("s3 subject marks: "))  

total_pracentege=(s1+s2+s3)/3

if(total_pracentege>=40 and s1>=33 and s2>=33 and s3>=33):
    print("pass in exam")
else:
    print("fail in exam")  '''
    
    
    
'''
#spam comment
a1="make a lot of money"
a2="buy now"
a3="subscribe this"
a4="click this" 

massage=input("enter the massage:")

if((a1 in massage) or (a2 in massage)or (a1 in massage) or (a2 in massage)):
    print("this massage is sapm")
else:
    print("this massage is save") '''
    
    
'''
# ten charactor or not

name=input("enter the name: ")

if len(name)<10:
  print("this charactor is less then 10 ")   
else:
  print("this charactor is not less then 10 ") '''

'''
#list
name=input("enter the name: ")
l=["swayam","vivek","maurya"]
if(name in l):
    print("this name is in list")
else:
    print("this name is not in list") '''

'''
#grade
marks=int(input("enter the marks:"))

if(marks<100 and marks>90):
    print("grats A")
elif(marks<90 and marks>80):
    print("grats b")
elif(marks<80 and marks>70):
    print("grats c")
elif(marks<70 and marks>60):
    print("grats d")
elif(marks<60 and marks>50):
    print("grats f")
elif(marks<50 ):
    print("grats g")'''
