#########
# class Gb:
#     def __init__(self):
#         print("Object Creating....")
#     def __del__(self):
#         print("Object Destroying....")
            
# aaa = Gb()
# aaa = None  

# # bb = Gb()
# cc = Gb()

# cc = None
# print(cc)


###############

# import time
# class A:
#     def __init__(self):
#         print("Object Creating....")
#     def __del__(self):
#         print("Object Destroying....")

        
# a = A()
# b = a
# c = a
# d = a

# time.sleep(2)
# del a
# print("deleting a")
# time.sleep(2)
# del b
# print("deleting b")
# time.sleep(2)
# del c
# print("deleting c")
# time.sleep(2)
# del d
# print("deleting d")


############

# import sys
# class A:
#     pass


# a = A()
# b = a
# c = a
# d = a
# print(sys.getrefcount(a))


############
# relation :


class Account:
    def __init__(self, accNo, accHolderName, accType , balance):
        self.accNo = accNo
        self.accHolderName = accHolderName
        self.accType = accType
        self.balance = balance
        
class Employee:
    def __init__(self, eno, ename, esal,eaddr, account):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.account = account      
        self.eaddr = eaddr    

    def getEmpDetails(self):
        print("Employee Details")
        print("-------------------")
        print("Employee Number :",self.eno)
        print("Employee Name :",self.ename)
        print("Employee Salary :",self.esal)
        print("Employee Address :",self.eaddr)
        print()
        print("Account Details")
        print("-------------------")
        print("Account Number :",self.account.accNo )     # self.account.accNo
        print("Account Holder Name :",self.account.accHolderName)
        print("Account Types :",self.account.accType)
        print("Account Balance :",self.account.balance)

        
aacc = Account("abc123", "Durga", "Savings", 25000)
emp = Employee("E-111", "Durga", 10000.0, "Hyd", aacc )
emp.getEmpDetails()
