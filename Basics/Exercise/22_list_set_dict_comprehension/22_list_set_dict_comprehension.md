## Exercise: List Set Dict Comprehensions


1. Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict. 

Example :
```
    integer = [0, 1, 2, 3, 4]
    binary = ["0", "1", "10", "11", "100"]
    binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}
```

2. Create a List which contains additive inverse of a given integer list. 
An additive inverse `a` for an integer `i` is a number such that:
```
a + i = 0
```
Create tuples inside a list as (i**2,i**3):

Example:
```
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

integer = [1, -1, 2, 3, 5, 0, -7]
squares_and_cubes = [(1, 1), (1, -1), (4, 8), (9, 27), (25, 125), (0, 0), (49, -343)]
```

3. Create a set which only contains unique sqaures from a given a integer list.
4. Create a set such that the value corresponding to i is i**2 when i is divisible by 2 else it's i**3:
```
integer = [1, -1, 2, -2, 3, -3]
sq_set = {1, 4, 9}

integer = [1, -1, 2, -2, 3, -3]
sq2_set = {1, 4, -27, 27, -1}
```

[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/22_list_set_dict_comprehension/22_list_set_dict_comprehension.py)
