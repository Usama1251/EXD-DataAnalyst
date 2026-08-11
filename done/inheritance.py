# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show_salary(self):
#         print(f"My salary is {self.salary}")
        
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary) #parent constructor ko call kr rha hai
#         self.department = department
        
#     def manage(self):
#         print(f"I manage the {self.department} department. ")

# e1 = Employee("Waleed", 150000)
# m1 = Manager("Usama", 60000, "AR Dept")

# e1.show_salary()
# m1.manage()

# protected is used as _ underscore
#private is used as double __ underscore

class Employee:
    def calculate_salary(self):
        baseSalary = 200000
        print(f"Salary is {baseSalary}")

class Manager(Employee):
    def calculate_salary(self):
        baseSalary = 210000
        print(f"Salary is {baseSalary}")

class Developer(Employee):
    def calculate_salary(self):
        baseSalary = 220000
        print(f"Salary is {baseSalary}")

e1 = Employee()
e1.calculate_salary()

m1 = Manager()
m1.calculate_salary()

d1 = Developer()
d1.calculate_salary()