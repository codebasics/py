def print_pattern(n=5):
    '''
    :param n: Integer number representing number of lines
    to be printed in a pattern. If n=3 it will print,
      *
      **
      ***
    If n=4, it will print,
      *
      **
      ***
      ****
    Default value for n is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
    '''
    # we need to run two for loops. Outer loop prints patterns line by line
    # where as inner loop print the content of that specific lines
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)

def calculate_area(dimension1,dimension2,shape="triangle"):
    '''
    :param dimension1: In case of triangle it is "base". For rectangle it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    '''
    if shape=="triangle":
        area=1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)
    elif shape=="rectangle":
        area=dimension1*dimension2 # Rectangle area is: Length*Width
    else:
        print("***Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area

# ------------------ Shape area exercise ------------------------- #
# Calculate area of triangle whose base is 10 and height is 5
base=10
height=5
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is:",triangle_area)

# Calculate area of a rectangle whose length is 20 and width is 30
length=20
width=30
rectangle_area=calculate_area(length,width,"rectangle")
print("Area of rectangle is:",rectangle_area)

# Calculate area of a triangle without supplying shape argument in a function call
triangle_area=calculate_area(base,height) # Here third argument is missing
print("Area of triangle with no shape supplied: ",triangle_area)

# -------------------- Pattern exercise ------------------------- #
print("Print pattern with input=3")
print_pattern(3)
print("Print pattern with input=4")
print_pattern(4)
print("Print pattern with no input number")
print_pattern() # Not supplying any input will use default argument which is 5


