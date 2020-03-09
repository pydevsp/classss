# def wish(name, message):
#  print("Hello",name,",",message)


# # wish()
# # wish("Anil")
# # wish("Nag", "Good Afternoon!")

# wish("good night",name="asis")

# def createAccount(accNo,accHolderName,accType="Savings", balance=10000):
#  print("Account Details")
#  print("----------------------")
#  print("Account Number :",accNo)
#  print("Account Holder Name :",accHolderName)
#  print("Account Type :",accType)
#  print("Account Balance :",balance)
# createAccount("abc123", "Durga")
# print()
# createAccount("xyz123", "Nag", "Current",100000)

# def add(a,b=20,c=30):
#  print(a+b+c)
# add(10,c=5)
# add(a=10)

# def add(a=10,b,c):       #    def add(a=10,b,c):
# print(a+b+c)             #                ^
# add(20,30)                #  SyntaxError: non-default argument follows default argument

# ==> Variable length Arguments:

# def voidfunc(a, b):
#   x = a + b
#   print(x)

# print(voidfunc(1, 2))



# def se(*n) :
#     print(n)                # *n ===>  "n" number of argument   , " * " means 0 ro, more element   

# se()
# se(10,"lhkjl",True,124.2)
# se(10,31,12,45,71,25,14)

# def fn (b=50,c=50,*a):
#     print(a)
#     print(b)
#     print(c)
#     print(a,b,c)

# fn(10,20,52,34,26,"aaa","vcc")


# def ss(a,b=50) :
#     print(a)
#     print(b)

# ss("aadf")
# a=10
# b=20
# def ad():
#     global a,b
#     a=30
#     b=42
#     def ad():
#         print(a,b)
#     ad()
# ad()

# def aas():
#     print(a,b)

# aas()

# def factValue (n) :
#     l = 1

#     if n == 0 :
#         l = 1
#     else :
#         l = n * factValue(n-1)
#     return l


# print(factValue(5))


def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n-1)     #     n!= n*(n-1)!

print(factorial(5))
# n=int(input("value :"))
# def fact(n) :
#     facto = 1
#     for i in range(1,n+1): 
#         facto = facto * i 
#     print(facto)



# print ("The factorial of %n is : ") 
# print (fact(n)) 

# facto = 1
# for i in range(1,6): 
#     print(i)



# print(facto)

### 2function 

def big(a,b) :
    if a<b :
        biNo = b
    else :
        biNo = a 
    return biNo





def compare (x, y , biggest) :
    print(x)
    print(y)
    print("big no. :", biggest(x,y))


compare(20,50,big)       #   "big"  function call as a argument of "biggest" 


# Python program to illustrate functions  
# can be passed as arguments to other functions  
# def shout(text):  
#     return text.upper()  
  
# def whisper(text):  
#     return text.lower()  
  
# def greet(func):  
#     # storing the function in a variable  
#     greeting = func("Hi, I am created by a function passed as an argument.")  
#     print(greeting) 
  
# greet(shout)  
# greet(whisper)  



# def f(n) :
#     while n>1 :
#         l= n *(n-1)
#         r=l
#         n=n-1
#     return(r)

# print(f(5))