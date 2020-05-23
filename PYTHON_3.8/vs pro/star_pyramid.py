# # # #pattern:24
# # # #-----------
# pyra=int(input("pyramid_height no:"))
# for x in range (1,pyra+1) :
#     print("="*(pyra-x),"* "*x,end="")   ### "* "*x ==> after * blank space requird for pyramid
#     print()


# # # # #pattern:24.1
# # # # #-------------
# pyra=int(input("pyramid_height no:"))
# for x in range (1,pyra+1) :
#     print(" "*(pyra-x),"* "*x)   
# print()


# # # #pattern:24.2
# # # #-------------
# pyra=int(input("pyramid_height no:"))
# for x in range (1,pyra+1) :
#     print(" "*(x-1),"* "*(pyra+1-x))
# print()

# # #pattern:24.3 
# # #-------------
# pyra=int(input("pyramid with odd nos. :"))
# for x in range(0,pyra) :
#     for y in range(0,pyra-x) :
#         print(" ",end="")
#     for z in range(0,2*x+1):
#         print("*",end="")
#     print()


# # #pattern:24.4 
# # #-------------
# pyra=int(input("pyramid with even nos. :"))
# for x in range(0,pyra) :
#     for y in range(0,pyra-x) :
#         print(" ",end="")
#     for z in range(0,2*x+2) :
#         print("*",end="")
#     print()



# # #pattern:24.5
# # #-------------
# pyra=int(input("pyramid with R-odd nos. :"))
# for x in range(0,pyra) :
#     for y in range(0,x) :
#         print(" ",end="")
#     for z in range(0,(pyra*2)-(2*x+1)) :
#         print("*",end="")
#     print()



# # #pattern:24.6
# # #-------------
# pyra=int(input("pyramid with R-even nos. :"))
# for x in range(0,pyra) :
#     for y in range(0,x) :
#         print(" ",end="")
#     for z in range(0,(pyra*2)-(2*x)) :
#         print("*",end="")
#     print()+



# #pattern:56
# #----------
di=int(input("diamond no. :"))
for x in range(1,di+1) :
    print(" "*(di-x),end="")
    for y in range(1,x+1):
        print("*",end=" ")
    print()
for a in range (1,di) :
    print(" "*a,end="")
    for b in range(1,di+1-a) :
        print("*",end=" ")
    print()