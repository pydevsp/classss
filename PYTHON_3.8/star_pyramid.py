# #pattern:24
# # #-----------
# pyra=int(input("pyramid_height no:"))
# for x in range (1,pyra+1) :
#     print("="*(pyra-x),"* "*x,end="")   # "* "*x ==> after * blank space requird for pyramid
# print()


# # #pattern:24.1
# # #-------------
# pyra=int(input("pyramid_height no:"))
# for x in range (1,pyra+1) :
#     print("="*(pyra-x),"*"*x)   
# print()


# #pattern:24.2
# #-------------
pyra=int(input("pyramid_height no:"))
for x in range (1,pyra+1) :
    print("="*(x-1),"* "*(pyra+1-x))
print()