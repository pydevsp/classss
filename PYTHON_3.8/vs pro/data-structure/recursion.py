# def find_uppercase_iterative(input_str):
#     for i in range(len(input_str)):
#         if input_str[i].isupper():           ##### .isupper()   ===> predefine func
#             print(input_str[i])

#     return "No uppercase character found"

# print(find_uppercase_iterative("InputStr"))



# def find_uppercase_recursive(input_str, idx=0):
#   if input_str[idx].isupper():
#     return input_str[idx]
#   if idx == len(input_str) - 1:
#     return "No uppercase character found"
#   return find_uppercase_recursive(input_str, idx+1)


# input_str_2 = "ucidProgramming"
# print(find_uppercase_recursive(input_str_2))



######################
# consonant :-  a e i o u

# vowels = "aeiou"

# def iterative_count_consonants(input_str):
#     consonant_count = 0
#     for i in range(len(input_str)):
#         if input_str[i].lower() not in vowels and input_str[i].isalpha():
#             consonant_count += 1
#     return consonant_count


# input_str = "abciide"
# print(input_str)
# print(iterative_count_consonants(input_str))


###################

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
print(fibonacci(7)) 