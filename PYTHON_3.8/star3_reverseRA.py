# #pattern:15
# #-----------

Rstar=int(input("R_ra_star range no :"))
for x in range(1,Rstar+1) :
    for y in range (1,Rstar+2-x) :
        print("* ",end="")
    print()      



# #pattern:16
# #-----------
Rnu=int(input("R_ra_numeric no :"))
for x in range (1,Rnu+1) :
    for y in range (1,Rnu+2-x) :
        print(x ,end="")
    print()




# #pattern:17
# #-----------
Rnu=int(input("R_ra_numeric_ver no :"))
for x in range (1,Rnu+1) :
    for y in range (1,Rnu+2-x) :
        print(y , end="")
    print()




# #pattern:18
# #------------
Rchar=int(input("R_ra_char_hor no :"))
for x in range (1,Rchar+1) :
    for y in range (1,Rchar+2-x) :
        print(chr(64+x),end="")
    print()



# #pattern:19
# #------------
Rchar=int(input("R_ra_char_ver no :"))
for x in range (1,Rchar+1) :
    for y in range (1,Rchar+2-x) :
        print(chr(64+y),end="")
    print()


# #pattern:20
# #------------

Rnu=int(input("R_ra_numeric_hor no :"))
for x in range (1,Rnu+1) :
    for y in range (1,Rnu+2-x) :
        print(Rnu+1-x ,end="")
    print()


# #pattern:21
# #------------
Rnu=int(input("R_ra_numeric_ver no :"))
for x in range (1,Rnu+1) :
    for y in range (1,Rnu+2-x) :
        print(Rnu+1-y , end="")
    print()


# #pattern:22
# #------------
Rchar=int(input("R_ra_Rchar_hor no :"))
for x in range (1,Rchar+1) :
    for y in range (1,Rchar+2-x) :
        print(chr(64+(Rchar+1-x)),end="")
    print()



# #pattern:23
# #------------
Rchar=int(input("R_ra_Rchar_hor no :"))
for x in range (1,Rchar+1) :
    for y in range (1,Rchar+2-x) :
        print(chr(64+(Rchar+1-y)),end="")
    print()