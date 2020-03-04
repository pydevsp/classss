A = "Shah Rukh Khan"
print("A ---",A)
print()

b= 'Shah Rukh Khan'
print("b ---",b)
print()
length = len(b)
print("length of b :",length)
print()
c = '''Shah Rukh Khan
       indian star'''     #multiline str
print("c ----",c)
print()

d = '\'shah\'"rukh" \'''khan\''' '
print(d)
print()

e = " 'shah' \"rukh\" '''khan''' "
print(e)
print()

f = ''' 'shah' "rukh" \'''khan\''' '''
print(f)
print()

# by index  // print(variable-name [index value])

print("##INDEX")
AA= 'shah Rukh Khan'
print(AA)
print(AA[0])
print(AA[1])
print(AA[2])
print(AA[3]) , print(AA[4]) , print(AA[5]) , print(AA[6]) , print(AA[7])
print(AA[8])
print()
print(AA[-1])
print(AA[-2])
print(AA[-3])
print(AA[-9])

## iterators 
print("\n")
for x in range (0,len(AA)) :
    print (x ," ==> ",AA[x])

print()

for x in range (0,len(AA)) :
    y = -(len(AA)-x)
    print(y ," ==> ",AA[y])

print()

for x in range (0,len(AA)) :
    y = -(len(AA)-x)
    print(y ," ==> ",AA[y])

print()

for x in range (0,len(AA)) :
    y = -(x+1)
    print(y ," ==> ",AA[y])

print("\n")
i = 0
while i<len(AA) :
    x = -(len(AA)-i)
    print(x,AA[x])
    i = i+1

## slice operator :
print('slice operator',"\n")
bb= "Shah Rukh Khan"
print(bb[ : : ])
print()
print(bb[: :1])
print()
print(bb[0: :1])
print()
print(bb[0:5:1])
print()
print(bb[:len(bb) :1])
print()
print(bb[0:-1 :1])
print()
print(bb[-1:10:-1])
print