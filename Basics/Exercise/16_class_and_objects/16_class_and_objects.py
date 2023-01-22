class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
            try:
                print(f"ID: {self.id} \nName: {self.name}")
            except AttributeError:
                print("ID is not defined")


# Creating a emp instance of Employee class
emp = Employee(1, "coder")

emp.display()

# Deleting the property of object
del emp.id

emp.display()

# Deleting the object itself
del emp

try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")
