# The main intention of Character classes is to search for group of
# characters in tarhet string.
# EX:
# a ----> It will find the match with exactly 'a'
# [abc] ----> It will find the match for either a or b or c
# [^abc] ---> It will find the match for the elements except a, b anc c.
# [a-z] ----> It will find the match for All lower case characters
# [A-Z] ----> It will find the match for all Upper case characters
# [a-zA-Z]---> It will find the match for all lowerr case and upper case
# matches.
# [0-9] -----> It will find the match for all digits.
# [^0-9] -----> It will find the match for allexcept digits.
# [a-zA-Z0-9] ---> It will find the match for all lower case , upper case
# characters and digits.
# . ------------> It will find the match for all characters ,digits, dots and
# special symbols.


import re
data = "abc123xyazMNL@dss.com"
# matcher = re.finditer("a",data)
# for match in matcher :
#     print(match.group(),match.start(),match.end())


##
# matcher = re.finditer("[a-z]",data)
# matcher = re.finditer("[^a-zA-Z0-9]",data)
# matcher = re.finditer("[a-zA-Z0-9]",data)
# matcher = re.finditer("[A-Z]",data)
# matcher = re.finditer("[^A-Z]",data)
# for match in matcher :
#     print(match.group(),match.start(),match.end())

    
##
# matcher = re.finditer("^abc",data)  ##### ======>  abc == ^abc 
# for match in matcher :
#     print(match.group(),match.start(),match.end()-1)








# #####################
# In Regular Expressions, we are able to use the following predefined
# characters to prepare patterns.
# \s ------> Represents Space
# \S ------> Represents all except space
# \d ------> Represents all digits
# \D ------> Represents all except digits
# \w ------> Represents all word characters [a-zA-Z0-9]
# \W ------> Represents all except word characters


import re
data = "abc123xyaz MNL@dss.com"
matcher = re.finditer("\D",data)
for match in matcher :
    print(match.group(),match.start(),match.end())



