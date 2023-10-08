class employee:
    def __init__(self, n, o ):
        self.name = n
        self.id = o

    def name_self(self):
        if self.id == '12':
            print(self.name, '12 years old')
        elif self.id == '18':
            print(self.name, '18 years old')

    def speaks(self):
        print(self.name, 'speaks how are you?')

enjoy = employee('Maqsat', '18')
enjoy.speaks()
enjoy.name_self()

# Creating a emp instance of Employee class
emp = Employee(1, "coder")

emp.display()
# Deleting the property of object
del emp.id
# Deleting the object itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")
