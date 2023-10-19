class animal:
    def __init__(self, habitat):
        self.habitat = habitat
    def print_habitat(self):
        print(self.habitat)
    def sound(self):
        print("Some Animal Sound")
class dog(Animal):
    def __init__(self):
        super().__init__("Kennel")
    def sound(self):
        print("Woof woof!")
x = Dog()
x.print_habitat()
x.sound()
