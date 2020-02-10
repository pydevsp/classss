# # pattern:1
# # ----------
# num = int(input("enter the nos. of row & column :"))
# for x in range (1,num+1) :
#     print("* "*num ,)

# print("=========")

# #pattern:2
# #----------

# num=int(input("enter the nos. of rows :"))
# for x in range(1,num+1) :
#     for y in range(1,num+1) :
#         print(x ,"", end="")
#     print("=")


# #pattern:3
# #----------

# N=int(input("enter the nos. of columns :"))

# for x in range (1,N+1) :
#     for y in range(1,N+1) :
#         print(y,"",end="")
#     print("=")


# #pattern:4.1
# #----------

# char=int(input("enter the nos. of rows :"))

# for x in range (1,char+1) :
#     for y in range (1,char+1) :
#         print(chr(64+1),"", end='')
#     print("=")



# print(chr(64))
# l=(chr(65))
# print(l)


# #pattern:4.2
# # ----------

# char=int(input("enter the nos. of rows :"))

# for x in range (1,char+1) :
#     for y in range (1,char+1) :
#         print(chr(64+x),"", end='')
#     print("=")



# #pattern:5
# #----------

# char=int(input("enter the nos. of rows :"))

# for x in range (1,char+1) :
#     for y in range (1,char+1) :
#         print(chr(64+y),"", end='')
#     print("=")


# #pattern:6
# #----------

# num=int(input("enter the nos. of rows :"))
# for x in range(1,num+1) :
#     for y in range(1,num+1) :
#         print((num+1)-x,"", end="")
#     print("=")



# #pattern:7
# #----------

# num=int(input("enter the nos. of rows :"))
# for x in range(1,num+1) :
#     for y in range(1,num+1) :
#         print((num+1)-y,"", end="")
#     print("=")



# #pattern:8
# #----------

Rchar=int(input("enter the nos. of rows :"))

for x in range (1,Rchar+1) :
    for y in range (1,Rchar+1) :
        print(chr(65+(Rchar-x)),"", end='')
    print("=")



# #pattern:9
# #----------

Rchar=int(input("enter the nos. of rows :"))

for x in range (1,Rchar+1) :
    for y in range (1,Rchar+1) :
        print(chr(65+(Rchar-y)),"", end='')
    print("=")
