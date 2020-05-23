# # association in python  :-
# # =========================
# ## One-To-One

# class Account:
#     def __init__(self, accNo, accHolderName, accType , balance):
#         self.accNo = accNo
#         self.accHolderName = accHolderName
#         self.accType = accType
#         self.balance = balance
        
# class Employee:
#     def __init__(self, eno, ename, esal,eaddr, account):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#         self.account = account      
#         self.eaddr = eaddr    

#     def getEmpDetails(self):
#         print("Employee Details")
#         print("-------------------")
#         print("Employee Number :",self.eno)
#         print("Employee Name :",self.ename)
#         print("Employee Salary :",self.esal)
#         print("Employee Address :",self.eaddr)
#         print()
#         print("Account Details")
#         print("-------------------")
#         print("Account Number :",self.account.accNo )     # self.account.accNo
#         print("Account Holder Name :",self.account.accHolderName)
#         print("Account Types :",self.account.accType)
#         print("Account Balance :",self.account.balance)

        
# acc = Account("abc123", "Durga", "Savings", 25000)
# emp = Employee("E-111", "Durga", 10000.0, "Hyd", acc )
# emp.getEmpDetails()



# ######2

# class School :
#     def __init__(self,mark1,mark2,mark3):
#         self.m1 = mark1
#         self.m2 = mark2
#         self.m3 = mark3

#     def Student(self,sname,rroo)






#### injection  

class Address :
    def __init__(self,hno,hname,street):
        self.hno = hno
        self.hname = hname
        self.street = street


class Course :
    def __init__(self,cid,cname):
        self.cid = cid
        self.cname = cname


class Student :
    def __init__(self,sid,sname,addr,courseList):
        self.sid = sid
        self.sname = sname
        self.addr = addr
        self.course = courseList

    def studentData (self):
        print("Student details")
        print("================")
        print("student Id     :", self.sid)
        print("student name   :",self.sname)
        print()

        print("Address details")
        print("================")
        print("House No.  :",self.addr.hno)
        print("House Name :",self.addr.hname)
        print("street     :",self.addr.street)
        print()
        print("course id \t course name")
        print("================================")
        for core in self.course :
            print(core.cid ,end="     \t       ")
            print(core.cname,end="\n")


course1 = Course("C-111", "C")
course2 = Course("C-222", "C++")
course3 = Course("C-333", "Java")
course4 = Course("C-444", "Python")
coursesList = [course1, course2, course3, course4]

addr = Address("202,23/3rt","MG house", "Hyd")
std = Student("S-111", "AAA", addr, coursesList)
std.studentData()
