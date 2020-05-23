# def is_anagram(s1, s2):
#     ht = dict()
#     print(ht)
#     if len(s1) != len(s2):
#         return False
        
#     for i in s1:
#         if i in ht:
#             ht[i] += 1
            
#         else:
#             ht[i] = 1
#     for i in s2:
#         if i in ht:
#             ht[i] -= 1
#         else:
#             ht[i] = 1
#     for i in ht:
#         if ht[i] != 0:
#             print(ht)
#             return False
#     return True

# s1 = "fairyy tales"
# s2 = "raill safety"
# ## normalizing the strings
# s1 = s1.replace(" ", "").lower()
# s2 = s2.replace(" ", "").lower()

# print(is_anagram(s1, s2))



####################

# def is_palin_perm(input_str):
#     input_str = input_str.replace(" ", "")
#     input_str = input_str.lower()

#     d = dict()

#     for i in input_str:

#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1

#     odd_count = 0
#     for k, v in d.items():
#         if v % 2 != 0 and odd_count == 0:
#             odd_count += 1
#         elif v % 2 != 0 and odd_count != 0:
#             return False
#     return True

# palin_perm = "Tact Coa"
# not_palin_perm = "This is not a palindromes"

# print(is_palin_perm(palin_perm))
# # print(is_palin_perm(not_palin_perm))


#############

# def is_perm_2(str_1, str_2):
#     str_1 = str_1.lower()
#     str_2 = str_2.lower()

#     if len(str_1) != len(str_2):
#         return False

#     d = dict()
    
#     for i in str_1:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     for i in str_2:
#         if i in d:
#             d[i] -= 1
#         else:
#             d[i] = 1
#     for value in d.values():
#         print(value)
#     return all(value ==0 for value in d.values())
# print()

# is_permutation_1 = "google"
# is_permutation_2 = "ooggle"

# not_permutation_1 = "not"
# not_permutation_2 = "top"

# print(is_perm_2(is_permutation_1, is_permutation_2))
# print(is_perm_2(not_permutation_1, not_permutation_2))

###############

def int_to_str(input_int):
    
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []
    while input_int > 0:
        output_str.append(chr(ord('0') + input_int % 10))
        input_int //= 10

    output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str


input_int = 123
print(input_int)
print(type(input_int))


output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))