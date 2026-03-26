class Employee:
    def __init__(self):
        self.id = int(input("Enter employee id: "))
        self.name  = input("Enter employee name: ")
        self.role = input("Enter employee role in the company: ")
        self.salary =  int(input("Enter employee salary: "))

    def display_info(self):
        print(f"ID (4 no.) : {self.id}, NAME : {self.name}, ROLE : {self.role}, SALARY (LPA) : {self.salary}")

soham = Employee()
rohan = Employee()

soham.display_info()
rohan.display_info()