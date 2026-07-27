# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"my name is {self.name}")
# student1 = student("Ali", 20)
# student2 = student("Usama", 30)

# print("Student 1 Name and Age ", student1.name, student1.age)
# # print("Student 2 Name and Age ", student2.name, student2.age)
# student1.introduce()

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def introduce(self):
#         print(f"{self.title}, {self.author}, {self.price}")
# book1 = Book("Title 1", "Author 1", 100)
# book1.introduce()

class Employee:
    company = "Google"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print("Employee Details", self.name, self.salary, self.company)
        
e1 = Employee("Ahmad", 21000)
e2 = Employee("Fatima", 30000)

e1.display()
e2.display()

Employee.company = "Microsoft"

e1.display()
e2.display()
