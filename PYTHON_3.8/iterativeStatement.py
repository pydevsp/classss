# # These statements are able to allow to execute a set of instructions repeatedly on the basis of a particular conditional expression.
# # EX: for, while

# # for var in range(start, end, step)/sequence_Data_Type:
# #    ----instructions------

# for x in range (10) :
#     print(x)
#     print(x,end=" ")





# # reverse print

# for x in range(10) :
#     print(10-x) 




# # display all even numbers from 0 to 20 ...
# n=range(0,20)
# for val in n :
#     if val % 2 ==0 :
#         print(val ,"is even number")

#     else :
#         print(val , "is odd number")




# #  prime number print ... 
# # a number that is divisible only by itself and 1

# num=int(input('enter value for  check prime or not : '))

# count=0
# for x in range (1,num+1) :
#     if num % x ==0 :
#         count = count+1
# if count ==2 :
#     print(num , "is prime number")
 
# else :
#     print(num , "is not prime number" ) 




# # print only prime number



# for x in range(2,no+1):
#     b = True
#     for y in range(1,x):
#         if not((y==1) or (y==x)) :
#             if x%y == 0:
#                 b = False

#     if b == True:
#         print("%d is Prime Number"%x)



# # generate all the prime nos. which are less then 50
# n= int(input("enter vALUE : "))

# for num in range(1,n+1) :
#     count=0
#     for x in range(1,n+1) :
#         if num % x ==0 :
#             count=count+1
#     if count==2 :
#         print(num ,"is prime number",)
#     else :
#         print(num ,"is not prime number")



# #star print
# for x in range(1,6):
#     print("*"*(6-x))

# #nested loop

for x in range(0, 10, 1):
    for y in range(0, 10, 1):
        if y==5 :
            break
        print(x,"  ", y ,end="")