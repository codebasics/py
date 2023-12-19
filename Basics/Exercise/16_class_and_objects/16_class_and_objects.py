class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


# Creating an emp instance of the Employee class
emp = Employee(1, "coder")

emp.display()
# Deleting the property of object
del emp.id
try:
    print(emp.id)
except AttributeError:
    print("emp.id is not defined")
# Deleting the object itself
del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")
