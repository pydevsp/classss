#pattern :10
#------------

RA_star=int(input("enter the no. of hight :"))
for x in range(1,RA_star+1) :
    print("* " * x )


#pattern :10.1 
#-------------

RA_star=int(input("enter the no. of hight :"))
for x in range(1,RA_star+1) :
    for y in range(1,x+1) :
        print("* ",end="" )
    print()


#pattern :11
#-------------

nu=int(input("numeric_RA_ver :"))
for i in range(1,nu+1) :
    for j in range(1,i+1) :
        print(i , end=" ")
    print()


# #pattern :12
# #-------------

nu=int(input("numeric_RA_hor :"))
for i in range(1,nu+1) :
    for j in range(1,i+1) :
        print(j , end=" ")
    print()


#pattern :13
#-------------

nu=int(input("char_RA_ver :"))                          
for i in range(1,nu+1) :
    for j in range(1,i+1) :
        print(chr(64+i) , end=" ")
    print()


# #pattern :14
# #-------------

nu=int(input("char_RA_ver :"))                          
for i in range(1,nu+1) :
    for j in range(1,i+1) :
        print(chr(64+j) , end=" ")
    print()




