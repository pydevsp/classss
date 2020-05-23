
# sqr = lambda x : x*x

# n = int(input("sqr of :"))
# print(sqr(n)) 
#  ===========================
# list = [5,10,15,20,25,30,35,40,45,50]

# val = filter(lambda x: x%2==0, list)

# for x in val:
#  print(x)
#  ===========================

# t = range(25,50)
# r = filter (lambda n : n>=25 and n<50 and n % 2 != 0,t )

# for  v in r :
#     print(v)

#  ===========================

# def addition(n): 
#     return n + n 
  
# # We double all numbers using map() 
# numbers = (1, 2, 3, 4) 
# result = map(addition, numbers) 
# print(set(result)) 

#  ===========================

# Double all numbers using map and lambda 
  
# numbers = (1, 2, 3, 4) 
# result = map(lambda x: x + x, numbers) 
# print(list(result)) 

#  ===========================

# from functools import *               ###  ' * ' means all module call
# list = [1,2,3,4,5,6,7,8,9,10]

# result = reduce(lambda x,y:x+y, list)
# print(result)

#  ===========================

def num1(x):
   def num2(y):
      return x * y
   return num2
res = num1(10)

print(res(1))


