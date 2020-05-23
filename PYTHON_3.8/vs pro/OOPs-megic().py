# class Student  :
#         def __init__(self,sid, sname, saddr, smarks):
#             self.sid = sid
#             self.sname = sname
#             self.saddr = saddr
#             self.smarks = smarks
            
#         def __lt__(self, other):
#             return self.smarks < other.smarks
        
#         def getStdDetails(self):
#             print(self.sid,"\t",self.sname,"\t",self.saddr,"\t",self.smarks)
            
        
        
# std1 = Student("S-111", "AAA", "Hyd", 78)
# std2 = Student("S-222", "BBB", "Hyd", 88)
# std3 = Student("S-333", "CCC", "Hyd", 67)
# std4 = Student("S-444", "DDD", "Hyd", 96)
# std5 = Student("S-555", "EEE", "Hyd", 58)

# stdList = [std1,std2,std3,std4,std5]


# while True:
#     count = 0
#     for x in range(0,len(stdList)-1):
#         if stdList[x] < stdList[x+1]:
#             pass
#         else:
#             count = count + 1
#             temp = stdList[x]
#             stdList[x] = stdList[x+1]
#             stdList[x+1] = temp
            
#     if count == 0:
#         break
#     else:
#         continue

        
# print("SID\tSNAME\tSADDR\tSMARKS")
# print("-----------------------------------")
#  for std in stdList:
#     std.getStdDetails()
                    

#######################
# 
# class Stud :
#     def __init__(self,sid , sname , smark):
#         self.sid = sid
#         self.sname = sname 
#         self.smark = smark
        
#     def __lt__(self , other) :
#         if self.smark < other.smark :
#             return self.sname+" last and "+other.sname+" fast."
#         elif other.smark < self.smark :
#             return self.sname+" fast and "+other.sname+" last ."
#         else :
#             return self.sname+" and "+other.sname+" equal ."
        
        
# std1 = Stud("s-11","AAA",82)
# std2 = Stud("s-22","BBB",67)
# std3 = Stud("s-33","CCC",90)

# print(std1<std2)
# print(std2<std3)
# print(std3<std1)                    





#####################

#Operator Overloading

## return object 
class Book:
    def __init__(self, name):
        self.name = name
    
    def __add__(self, other):
        new_name = self.name + " "+ other.name
        print(" __add___ ==>>",new_name)
        new_book = Book(new_name)
        return new_book

    
    
book1 = Book("book one name")    
book2 = Book("book two name")
book3 = Book("book three name")
book4 = Book("book four name")
result = book1 + book2 
result1 = result + book3
result2 = result1 + book4

print()
print(result2.name)
print(type(result2))
print(type(book1))