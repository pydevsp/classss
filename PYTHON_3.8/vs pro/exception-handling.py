# a = 10 
# b = 0
# # a/b 
# try :
#     print("inside try 1")
#     print(a/b)
#     print("inside try 2")
# except :
#     print("inside except")
# else :
#     print("inside else")
# finally :
#     print("inside finally")

# print("\n")

# print("hello")
# print(10/0)        # python default exception handling  ====   ZeroDivisionError: division by zero
# print("hiii")      # it is not execute




# acc statement :-

class InsufficientFundsException(Exception):
     def __init__(self, exceptionDescription):
         self.exceptionDescription = exceptionDescription
class Transaction:
     def __init__(self, accNo, accHolderName, accType, balance):
         self.accNo = accNo
         self.accHolderName = accHolderName
         self.accType = accType
         self.balance = balance
            
     def withdraw(self, wdAmt):
         print("Transaction Details")
         print("------------------------")
         print("Account Number :", self.accNo)
         print("Account Holder Name :", self.accHolderName)
         print("Account Type :",self.accType)
         print("Transaction Type : WITHDRAW")
         print("Withdraw Amount :",wdAmt)
            
            
         try:
             if wdAmt > self.balance:
                 print("Total Balance :", self.balance)
                 print("Transaction Status : FAILURE")
                 raise InsufficientFundsException("Reasone : Funds are not Sufficient in Your Account")
             else:
                 self.balance = self.balance - wdAmt
                 print("Total Balance :", self.balance)
                 print("Transaction Status : SUCCESS")
         except InsufficientFundsException as ex:
             print(ex)

         finally:
             print("******ThanQ, Visit Again********")
                
                
tx1 = Transaction("abc123", "Durga", "Savings", 10000)
tx1.withdraw(5000)
print("\n")
tx1 = Transaction("xyz123", "Anil", "Savings", 10000)
tx1.withdraw(15000)
