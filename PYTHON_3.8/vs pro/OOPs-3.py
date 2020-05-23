class Employee :

    no_of_leaves = 7

    def details(self):
        return f"Name is {self.name} . Salary is {self.salary} and role is {self.role}"
               # f or, F ==> f-sring  ======> str.format() ==> %

emp1 = Employee()
emp2 = Employee()

emp1.name = "sachin"
emp1.salary = 500000 
emp1.role = "visor"



print(emp1.details())

print(emp2.no_of_leaves)

