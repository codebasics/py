class AdultException(Exception):
    pass

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def get_minor_age(self):
        try:
            if self.age < 18:
                print(f"Age:{self.age}")
            else:
                raise AdultException
        except AdultException:
            print("Person is adult")
        finally:
            print(f"name:{self.name}")
            
pe = Person("Soumya", 19)
pe.get_minor_age()
