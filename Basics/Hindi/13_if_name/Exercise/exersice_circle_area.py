def circle_area(radius):
    return 22/7*radius**2

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle :"))
    area = circle_area(radius)
    print("Area of the circle :", area)
