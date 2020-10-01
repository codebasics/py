max = int(input("Enter max number: "))

odd_numbers = []

for i in range(max):
    if i%2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ",odd_numbers)


#we can also used list_comprehension to find the odd numbers
n = int(input("Enter a max number:"))
odd = [i for i in range(n) if i%2==1]
print("Odd Numbers : ",odd)
