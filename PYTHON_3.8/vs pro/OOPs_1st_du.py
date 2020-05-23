# create class
# class MyClass :
#     a = 10
   

# print(MyClass)   # o/p ==> <class '__main__.MyClass'>

# create object
# class TwoClass :
#     a = 20
   

# mcl=TwoClass()
# print(mcl.a)


# class Employee() :
#     eno = 100
#     ename = "SACHIN"
#     esal = 50000
#     eaddr = '''d colony 
#                 street 
#                 p-jeypore 
#                 s-odisha'''
    
#     def getEmpDetails(self) :
#         print("  Emp Details  ")
#         print("------------------")
#         print("Emp_no.     :",self.eno)
#         print("Emp_Name    :",self.ename)
#         print("Emp_salary  :",self.esal)
#         return ("Emp_address :{}" .format(self.eaddr))
       
        
# emp = Employee()
# print(emp.getEmpDetails())



# self :

# class A:
#     a = 10
#     b = 20
#     def m1(self):
#         print("m1-Method")
#         print(self.a)
#         print(self.b)
#         self.m2()
#         self.me()
        
#     def m2(self):
#         print("m2-Method")
#         print(self.a)
#         print(self.b)
#         self.me()

#     def me (self):
#         print("me-methods")
        
# a = A()
# a.m1()

#  ==>Class and Instance Attributes
# -----------------------------------
# class A:
#     a = "I am a class attribute!"
#     print(a)


# x = A()
# y = A()
# x.a 
# #o/p ==> 'I am a class attribute!'
# print(y.a)
# #o/p ==> 'I am a class attribute!'
# print(A.a)
# # o/p ==>  'I am a class attribute!'
# x.a = "This creates a new instance attribute for x!"
# A.a = "This is changing the class attribute 'a'!"
# print(A.a)
# #"This is changing the class attribute 'a'!"
# print(y.a)
# #"This is changing the class attribute 'a'!"


# # but x.a is still the previously created instance variable:

# print(x.a)
# #'This creates a new instance attribute for x!'



### OOP's d-video
#1
class Student :
    def __init__(self,name,rno,mark) :
        self.sname = name
        self.srollno = rno
        self.smark = mark


st = Student("aaa",1,80)
print(st)
print(st.sname,st.srollno,st.smark)

st2 = Student("bbb",2,82)
print(st2.sname,st2.srollno,st2.smark)


print()

#2
class Stu :
    ''' STUDENT DATA ''' ### DOC-STRING
    def __init__(self,a,b,c) :
        self.sname = a
        self.sno = b
        self.smark = c 
    
    def display(self):
        print("student name :{} , rollno :{} , mark :{}" .format(self.sname,self.sno,self.smark))


su = Stu("AA",1001,52)
su.display()
print(su.__doc__)


print()

#3
class Stud :
    ''' STUDENT DATA ''' ### DOC-STRING
    def __init__(self,a,b,c) :
        self.sname = a   #### a, b, c ====> Instance Variable 
        self.sno = b
        self.smark = c 
    
    def display(self):
        print(self.__doc__)
        print("==============")
        print("student name :{} , rollno :{} , mark :{}" .format(self.sname,self.sno,self.smark))


suu = Stud("AaaA",1001,52)
suu.display()

au = Stud("BbbB",1002,80)
au.display()

print()


#4 === static variable

class Cstudent :
    college = "durgasoft"  # static variable value
    def m1(self):
        self.college = "DURGASOFT"


cs=Cstudent()
print(cs.college)
print(Cstudent.college)
print(cs.m1())
print(Cstudent.college)
print(cs.college)   #### change static value ===> cs.m1 
print(cs.college)


print()
#5

class Studentss:
    '''this is Studentss properties and actions'''
    pass


print(Studentss.__doc__)