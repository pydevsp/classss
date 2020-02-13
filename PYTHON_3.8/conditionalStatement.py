a=float(input("enter value: "))
b=float(input("enter value: "))
c=float(input("enter value: "))

if a>b :
    if a>c :
        print("%d is biggest no."%a)
    else:
        print("%d is biggest no."%c)
elif b>c:
    if b>a :
        print("%d is biggest no."%b)
    else :
        print("%d is bigggest no."%a)
elif c>a :
    if c>b :
        print("%s is biggest no."%c)
    else :
        print("%d is biggest no."%b)
else :
    print("all nos. are equal")
    
print(type(a),"a")
print(type(b),"b")
print(type(c),"c")


v1=float(input("enter valus:"))
v2=float(input("enter valus: "))
if v1>v2 :
     print("%i is big no."%v1)
elif v2>v1 :
     print("%i is big no."%v2)
else :
     print("two equal nos.")



day=int(input("week no.: "))
if day==1 :
    print('today sunday')
elif day==2 :
    print('today monday')
elif day==3 :
    print('today tuesday')
elif day==4 :
    print('tody wednesday')
elif day==5 :
    print('today thursday')
elif day==6 :
    print("today friday")
elif day==7:
    print('today saturday')
else:
    print("put only 1-7 no.")


name =input("name: ")
if name=="ram" :
    print("you successfully accessed")
else:
    print("your name is not ram ,your name is %s"%name)




no = int(input("Enter a Number : "))
if no % 2 == 0 :
    print("%d is Even Number"%no)
else:
    print("%d is Odd NUmber"%no)


n1=int(input("enter value :"))
n2=int(input("enter value :"))
n3=int(input("enter value :"))

if n1>=n2 and n1>n3 :
    print(n1 , "is big no.")
elif n2>=n1 and n2>n3 :
    print(n2 , "is bi no.")
elif n3>=n1 and n3>n2 :
    print(n3 ,"is big no.")
else :
    print("all 3nos. equal")


# Rstar=input()      # input() function o/p str datatype
# print(Rstar)
# print(type(Rstar))

# i/p = 5
# o/p = 5
#       <class 'str'>