# def array_advance(A):
#     furthest_reached = 0
#     last_idx = len(A) - 1
#     i = 0
#     while i <= furthest_reached and furthest_reached < last_idx:
#         furthest_reached = max(furthest_reached, A[i] + i)
#         i += 1
#     return furthest_reached >= last_idx


# # True: Possible to navigate to last index in A:
# # Moves: 1,3,2
# A = [3, 3, 1, 0, 2, 0, 1]
# print(array_advance(A))

# # False: Not possible to navigate to last index in A:
# A = [3, 2, 0, 0, 2, 0, 1]
# print(array_advance(A))


#################

# A = [1, 4, 9]
# s = list(map(str, A))
# j = "".join(s)
# print(s)
# print(j)

# print(int(j) + 1)


#################

# A1 = [1, 4, 9]
# A2 = [9, 9, 9]

# # s = ''.join(map(str, A))
# # print(int(s) + 1)

# def plus_one(A):
#     A[-1] += 1
#     for i in reversed(range(1, len(A))):
#         if A[i] != 10:
#             break
#         A[i] = 0
#         A[i-1] += 1
#     if A[0] == 10:
#         A[0] = 1
#         A.append(0)
#     return A


# print(plus_one(A1))
# print(plus_one(A2))

####################
# two sum

def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]   ## ht[15]  ===> key==>{15:},{12:}
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum_hash_table(A, target))
##
d = {15:-2,12:1,1:20,9:4,6:7,2:11}
for i in range(len(A)):
    if A[i] in d:      #### dict key
        # print(A[i])        
        print(d[A[i]])   ### dict value of A[i ]

