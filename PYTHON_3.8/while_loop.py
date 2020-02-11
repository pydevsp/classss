str = "Durga Software Solutions"

a = 0
while a < len(str):
    print(str[a])
    a = a+ 1




a=int(input("enter value :"))
if a>1 :
    for x in range(2,a) :
        if a % x ==0 :
            print(a ,"not prime no")
            break
    else :
        print(a ,"is a prime no")



#  fibonacci serise number print

n=int(input("range value :"))

fpoint=0
spoint=1
fibopoint=fpoint+spoint
print(fpoint)
print(spoint)
while fibopoint <= n :
    print(fibopoint)
    fpoint=spoint
    spoint=fibopoint
    fibopoint=fpoint+spoint


#with for loop
n=int(input("range value :"))

fpoint=0
spoint=1

for i in range (n) :
    print(fpoint)
    new=fpoint
    fpoint=spoint
    spoint=new+spoint
            