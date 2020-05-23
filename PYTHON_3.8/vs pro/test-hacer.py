# def is_leap(year):
#     leap = False
#     n = year
#     if n % 400 == 0:
#         return True
#     if n % 100 == 0:
#         return False
#     if n % 4 == 0:
#         return True
#     return False
#     return leap

# year = int(input())
# print(is_leap(year))


# N = int(input("value :"))
# for x in range(1,N+1):
#     print(x ,end='')



# def add(a,b):
#  print(a+b)


# add(10,20)

# print(add(45,50))


# def show_excitement():
#     t = "I am super excited for this course!"
#     return (t)

# print (show_excitement())

###############################
# n = int(input("ent : "))

# nums = map(int, input("list :").split())    
# So = sorted(list(set(nums)))
# print(So)
# print(So[-2])

# nums =input("list :").split()
# D = map(int , nums)
# print(D)
# E = set(D)
# print(E)
# # F = sorted(E)[-2: : ]
# # print(F)

# s = sorted([5,0,8,2,5,12,1,6,10, 3, 1, 4])
# S = set(s)
# L = list(S)
# print(L)
# print(L[-2])
###################################
#count_substring
# def count_substring(string, sub_string):
#     count=0
#     #print(len(string),len(sub_string))
#     for i in range(0, len(string)-len(sub_string)+1):
#         if string[i] == sub_string[0]:
#             flag=1
#             for j in range (0, len(sub_string)):
#                 if string[i+j] != sub_string[j]:
#                     flag=0
#                     break
#             if flag==1:
#                 count += 1
#     return count


# string = input().strip()
# sub_string = input().strip()
# print(len(string),len(sub_string))    
# count = count_substring(string, sub_string)
# print(count)


############################################
# thickness = int(input())
# c = "H"
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))







############
# from  collections import Counter  as co

# s = (input())
# s = sorted(s)
# z = co(s)
# print(z)
# z = co(s).most_common(3)
# print(z)

# for x in z :
#     print(x[0],x[1])

## info :
# from collections import Counter
# cnt = Counter({1:3,2:4})
# print(list(cnt.elements()))


##
# from collections import Counter
# cnt = Counter({1:3,2:4})
# deduct = {1:1, 2:2}
# cnt.subtract(deduct)
# print(cnt)



############### open close brackets [[]] == true ,[[)] == false
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    
    
print(is_paren_balanced("[[]]"))