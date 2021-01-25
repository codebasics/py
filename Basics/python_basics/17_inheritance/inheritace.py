class Animal:
  def __init__(self, living_place):
    self.living_place = living_place

  def printplace(self):
    print(self.living_place)

class Dog(Animal):
  def __init__(self, living_place):
    super().__init__(living_place)

x = Dog("zoo")
x.printplace()

