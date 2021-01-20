class Employee:  
    
    def __init__(self,id,name):
        self.id=id
        self.name=name
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  

# Creating a emp instance of Employee class    
emp = Employee(1,"coder")  
  
# Deleting the property of object  
# del emp.id  
# Deleting the object itself 
emp.display()  


#del emp  
#emp.display()  #it will gives error after del emp