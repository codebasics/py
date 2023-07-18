# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads
print("\nExercise 1\n")
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
print("Heads count: ",result.count('heads')


# 2. Print square of all numbers between 1 to 10 except even numbers
print("\nExercise 2\n")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
print("\nExercise 3\n")
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')

# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

print("\nExercise 4\n")
#this time module has the sleep method that helps to print the output of for above problem interactively...
# this time module synchroniZes cpu with the STDOUT and output iss displayed much lively...
import time
try:
    rounds=int(input("How many rounds did you set as your goal? "))
    if(rounds<1):
        raise ValueError
except ValueError:
    print("Your rounds must be Natural Number only")
    exit()

print("OK")
time.sleep(1)
print("get",end="\t")
time.sleep(1)
print("set",end="\t")
time.sleep(1)
print("Go!!!")
for i in range(rounds):
    time.sleep(2)
    print(f"Oh you compleated {i+1} rounds")
    time.sleep(0.7)
    if i==rounds-1:
        print("Hurray you compleated the race...")
        exit()
    isTired=input("Are you tired? (yes/no): ")
    if isTired=='yes':
        print("Oh you lost the race...")
        break
    else:
        print("All the best continue you race...")
        continue

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
print("\nExercise 5\n")

list=['*'*i for i in range(1,6)]
for i in list:
    print(i)
