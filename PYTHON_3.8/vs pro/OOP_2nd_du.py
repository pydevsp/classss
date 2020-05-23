# class Employee :
#     eno = 111
#     def __init__(self):
#         self.eno =self.eno 
#         self.ename = "aaa"

# emp = Employee()
# print(emp.__dict__)  ## instance value o/p

# class A:
#     i = 10
#     j = 20
#     k = 30
#     l = 40
#     m = 50
#     n = 60
#     def __init__(self):
#         del A.i
#     def m1(self):
#         del A.j
#         print("instance method")
#     @classmethod
#     def m2(cls):
#         print("class method")
#         del A.k
#         del cls.l
#     @staticmethod
#     def m3():
#         print("static method")
#         del A.m

# print(A.__dict__)
# a = A()
# print(A.__dict__)
# a.m1() 
# print(A.__dict__)
# A.m2()
# print(A.__dict__)
# A.m3()
# print(A.__dict__)
# del A.n
# print(A.__dict__)

## static instance variable

# class A :
#     i = 10


# print(A.__dict__)    ### {"i":10 , different all data}



# class Ab :
#     i = 10
#     def __init__(self):
#         A.j = 20



# # print(A.__dict__) ####{}
# a = Ab()
# print(a.__dict__)  ###{"i":10,.........,"j":20}
# print(10)


##### ticket print
class Bookshow():
    def __init__(self,name,sno,order) :
        self.name = name
        self.sno = sno
        self.order = order
    
    def Customer(self) :
        print("name      :", self.name)
        print("sheet no. :",self.sno)
    
    def Order(self) :
        if self.order == "yes":
            return("is ordered")
        elif self.order == "no":
            return("not ordered")
        else:
            return("----")

    def Cust_detail(self):
        print("name          :", self.name)
        print("sheet no.     :",self.sno)
        print("popcorn Order :",bms.Order())


bms = Bookshow(input("name :") ,input("sheet no :")  , input("popcorn yes/no :"))
bms.Cust_detail()