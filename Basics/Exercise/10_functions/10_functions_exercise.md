# Exercise: Functions in python
1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
```
def calculate_area(base, height):
    """
    Calculate the area of a triangle given its base and height.

    Args:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    area = 0.5 * base * height
    return area

```

2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
``vdef calculate_area(base, height, shape="triangle"):
    """
    Calculate the area of a shape given its base and height.

    Args:
    base (float): The base of the shape.
    height (float): The height of the shape.
    shape (str): The type of shape, can be "triangle" or "rectangle".

    Returns:
    float: The area of the shape.
    """
    if shape == "triangle":
        area = 0.5 * base * height
    elif shape == "rectangle":
        area = base * height
    else:
        print("Invalid shape type. Defaulting to triangle.")
        area = 0.5 * base * height
    return area

```
If no shape is supplied then it should take triangle as a default shape

3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
```
def print_pattern(num):
    """
    Print a pattern based on the input number.

    Args:
    num (int): The number of lines to print in the pattern.
    """
    for i in range(1, num + 1):
        for j in range(i):
            print("*", end="")
        print()

```
if input is 4 then it should print
```
*
**
***
****
```
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/10_functions/10_functions_exercise.py)
