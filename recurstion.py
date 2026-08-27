'''
🔁 Recursion (Definition)
🇬🇧 English:

Recursion is a programming technique where a function calls itself to solve a problem.

🇮🇳 हिंदी:

Recursion एक ऐसी तकनीक है जिसमें function खुद को ही बार-बार call करता है ताकि problem 
को solve किया जा सके।

🧠 How Recursion Works (कैसे काम करता है)
🇬🇧 English:

A recursive function keeps calling itself until a stopping condition (base case)
is reached.

⚙️ Two Important Parts (2 जरूरी हिस्से)
1. Base Case (Stopping Condition)
🇬🇧 English:

The condition where recursion stops.

2. Recursive Call
🇬🇧 English:

The function calling itself.
'''
'''
def fun(n):
    if n==0:
        return 
    print(n)
    fun(n-1)
fun(3)

fun(3)
 → print 3
 → fun(2)
     → print 2
     → fun(1)
         → print 1
         → fun(0)  (stop) '''
'''
#1Q factorial
def fac(n):
    if n==0:
       return 1
    return n*fac(n-1)
n=int(input("enter the number="))
print(fac(n))
'''
# 2Q fibonacci🇬🇧 English:
'''
Fibonacci series is:
0, 1, 1, 2, 3, 5, 8...

Each number = sum of previous two numbers'''

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input("enter the number="))

for i in range(n):
 print(fib(i),end=" ")