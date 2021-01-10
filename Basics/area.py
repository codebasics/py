# IT will calculate the area of a triangle
# Area of Traingle is=1/2*Base*Height
def calculate_area(base, height):
    print("__name__: ",__name__)
    return 1/2*(base*height)

if __name__ == "__main__":
    print("I am in area.py")
    a=calculate_area(10, 20)
    print("area: ",a)
