# Dictionary
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

z = zip(integer, binary)
binary_dict = {integer: binary for integer, binary in z}

print(binary_dict)

# List
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1*i for i in integer]
print(additive_inverse)

# List - Squares & Cubes
squares_and_cubes = [(i**2,i**3) for i in integer]
print(squares_and_cubes)

# Set
integer = [1, -1, 2, -2, 3, -3]
sq_set = {i*i for i in integer}
print(sq_set)

# Set - if/else included inside the comprehension
sq2_set = {i**2 if i%2 == 0 else i**3 for i in integer }
print(sq2_set)
