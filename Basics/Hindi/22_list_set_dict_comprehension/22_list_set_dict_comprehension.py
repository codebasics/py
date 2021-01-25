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

# Set
integer = [1, -1, 2, -2, 3, -3]
sq_set = {i*i for i in integer}
print(sq_set)
