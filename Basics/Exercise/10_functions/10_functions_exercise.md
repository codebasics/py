# Exercise: Functions in python
1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
```
area = (1/2)*base*height
```

2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
```
rectangle area=length*width
```
If no shape is supplied then it should take triangle as a default shape

def calculate_area(base,hight):
        area=(1/2)*base*hight
        return area
def calculate_area(length,width):
        area=length*width
        return area

shape_type=str(input('shape of object : '))
if shape_type=='triangle':
        base=int(input('enter the value of base:'))
        hight=int(input('enter the value of hight :'))
        total=calculate_area(base,hight)
        print('total area of triangle is :',total)
elif shape_type=='rectangle':
        length=int(input('enter the value of length:'))
        width=int(input('enter the value of width:'))
        total=calculate_area(length,width)
        print('total area of triangle is :',total)
#If no shape is supplied then it should take triangle as a default shape
else:
        print(' you enterd shape is not defined so it takes the shape as triangle as default ')
        base = int(input('enter the value of base:'))
        hight = int(input('enter the value of hight :'))
        total = calculate_area(base, hight)
        print('total area of triangle is :', total)



3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
```
*
**
***
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
