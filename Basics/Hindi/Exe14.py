"""
Make a program which have function named circle_area which takes one argument, radius, to calculate the area of the circle.
Taking pie = 22/7With the help of if __name__ == '__main__' function, show the output to the user."""

"""Solution""" 
def circle_area(radius):
    return 22/7*radius**2

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle :"))
    area = circle_area(radius)
    print("Area of the circle :", area)