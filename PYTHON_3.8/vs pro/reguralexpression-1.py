##Q)Find the no of occurences of the word Durga and its starting and
###ending positions in String data ?

# data = '''Durga Software Solutions is very good Org for IT Courses, DurgaSoftware 
# Solutions has no of branches, Durga Software Solutions has very
# good trainer in the form of Durga sir''' 

import re 
# matcher = re.finditer("Durga",data)
# count = 0
# for match in matcher :
#     count = count+1
#     print(match.group() , "====>", match.start(),"===>",match.end()-1)
# print("no of occurences  :",count)



####################################################

##Q)Find the no of occurences of the word Durga and its starting and
### ending positions in String data existed in a text file?


# data = '''Durga Software Solutions is very good Org for IT Courses, DurgaSoftware 
# Solutions has no of branches, Durga Software Solutions has very
# good trainer in the form of Durga sir'''

import re
file = open("c:/classss/ABC/redata.txt","r")
# pattern = "Durga"
# count = 0
# for line in file:
#     matcher = re.finditer(pattern,line)
#     for match in matcher:
#         count = count + 1
#         print(match.start(),"--->",match.end()-1,"--->",match.group())
# print("No of Occurences :",count)

## 2ND METHOD
data = file.read()
count = 0
for match in re.finditer("Durga",data) :
    count = count+1
    print(match.start(),"--->",match.end()-1,"--->",match.group())
print("No of Occurences :",count)