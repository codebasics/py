# 1. Use python to find area of triangle
# area = (1/2)*base*height
base=10.26
height=20.572
area=(1/2)*base*height
print("area is:",area) # area is: 105.53435999999999
# to show area till 2 decimal places
print("area rounded to 2 decimal place:",round(area,2)) # 105.53

# 2. basic airthmetic using numbers
print(1+2) # 3
print(1/2) # 0.5
print(17%3) # 2
print(3**2) # 9
print(10+2*3) # 16
print((10+2)*3) # 36

# 3. Number data types (int, float, complex numbers)
print(type(area)) # float
foo=2.3e-3
print(foo) # 0.0023
print(type(1)) # int
print(0x12) # 18
print(type(0x12)) # int
c1=2+3j
print(type(c1)) # complex
c2=3-4j
print(c1+c2) # 5-j

# 4. Internal representation of numbers
# (a) integers are stored in simple binary format
print(format(5,'b')) # 4 bytes (or 32 bits), visual of binary presentation
# (b) floats use IEEE754 standard : https://en.wikipedia.org/wiki/IEEE_754
print(6-5.7) # this prints 0.29999999 and not 0.3. why? Due to IEEE 754 standard



