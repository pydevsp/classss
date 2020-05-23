def first_n(num):
    n = 1
    while n <= num:
        yield n*10
        n = n + 1



values = first_n(5)
l = list(values)
print(l)
