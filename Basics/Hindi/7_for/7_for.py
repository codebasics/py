# expense total using simple sum
expenses = [1200,1500,1300,1700]
total = expenses[0] + expenses[1] + expenses[2] + expenses[3]
print(total)

# expense total using for loop
total = 0
for expense in expenses:
    total = total + expense
print(total)

# explain for loop iterations by debugging code

# range() function
print(range(1,11))
print(list(range(1,11)))
for i in range(1,11):
    print(i)

# in monthly expense list print month number, expense and then total
total = 0
for i in range(len(expenses)):
    print(f"Month {i+1}, expense: {expenses[i]}")
    total += expenses[i]
print(f"Total expenses is {total}")

# break
key_location="chair"
locations = ["sofa","garage","chair","table","closet"]
for loc in locations:
    if loc == key_location:
        print("Key found at:",loc)
        break
    else:
        print("Key not found in:",loc)

# continue: print odd numbers between 1 to 10
for i in range(11):
    if i%2==0:
        continue
    print(i)

# while loop
num=0
while num<=10:
    print(num)
    num=num+1