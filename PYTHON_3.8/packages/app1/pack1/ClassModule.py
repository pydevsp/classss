class Student:
    sId = input("sid          : ")
    sName = input("sName      :")
    sAddr = input("sAddr      :")
    sPhone = input("phone no. :")


    def get_student_details(self):
        print(" Student data")
        print("==============")
        print("Student ID             :" , self.sId)
        print("Student Name           :" , self.sName)
        print("Student address        :" , self.sAddr)
        print("Student Phone no.      :" , self.sPhone)


std=Student()



