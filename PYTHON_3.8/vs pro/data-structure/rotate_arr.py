def rotateArr(d, n, list):
    list[0:d] = reversed(list[0:d])   # count reverce nos.
    list[d:n] = reversed(list[d:n])   # skip part reverce
    list[0:n] = reversed(list[0:n])   # total reverce



# take n and d input
n_d = [int(x) for x in input().strip().split()]
n = n_d[0]
d = n_d[1]
list = [int(x) for x in input().strip().split()]

# call the rotate function
rotateArr(d, n, list)

# print the list
for i in range(n):
    print(list[i], end=" ")


