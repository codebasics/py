class Father:
  def __init__(self, name, lastname):
    self.name = name
    self.lastname = lastname

  def printname(self):
    print(self.name, self.lastname)

class Son(Father):
  def __init__(self, name, lastname):
    super().__init__(name, lastname)

x = Son("Darshan", "Beladiya")
x.printname()

