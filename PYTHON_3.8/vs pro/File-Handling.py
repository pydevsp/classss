import os 

# file = open("c:/classss/ABC/hello.txt" , "w")
# print("File mode          :" , file.mode)
# print("File Name          :" , os.path.basename(file.name))
# print("File Directory     :",os.path.dirname(file.name))           ## Get Parent location :
# print("Absolute Path      :",file.name)
# print("Absolute Path      :",os.path.abspath(file.name))
# print("Is Readable        :",file.readable())
# print("Is Writable        :",file.writable())



### dynamically read file
# fileName = input("Enter File Name : ")
# file = open(fileName,'r')
# data = file.read()
# print(data)           #### i/p ===> file path

########################################
##### -Q)Write a python program to take file name as dynamic input and to display no of lines, no of words 
# and no of characters of the respective file?

# filePut = input("enter file path : ")
# File = open(filePut,"r")
# data = (File.read())
# print(data)
# len(data)

# lines = 0
# words = 0
# chars = 0
# File.seek(0)

# # lines = data.count("\n")
# # print(lines)
# # words = len(data.split())
# # print(words)
# # chars = len(data)
# # print(chars)

# for li in File :
#     lines = lines+1
#     words = words+len(li.split())
#     for wo in li.split() :
#         chars = chars + len(wo)

# print()
# print(lines)
# print(words)
# print(chars)


###############################################

# f = open("c:/classss/ABC/2end.txt","r+")
# data = f.readlines()
# print(data)
# for s in data :
#     print(s)



a = "44646"
b = "53466331313"
print(a,"\n",b)