## Exercise: Python If Condition
1. Using following list of cities per country,
    ```
    india = ["mumbai", "banglore", "chennai", "delhi"]
    pakistan = ["lahore","karachi","islamabad"]
    bangladesh = ["dhaka", "khulna", "rangpur"]
    ```
    1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
    
    india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city=input('enter an city name')
if city in india:
    print(f'{city}  prasent in india')
elif city in pakistan:
    print('the city are',city,'in pakistan')  
elif city in bangladesh:
    print(f'{city} city is prasent in bangladesh')
else:
    print(city,' does not belongs to these contry')
    
    2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city1=input('enter an city name:')
city2=input('enter an city name:')
if city1 and city2 in india:
    print(f'{city1}{city2} both are prasent in india')
elif city1 and city2 in pakistan:
    print('the both citys are',city1,city2,'in pakistan')  
elif city1 and city2 in bangladesh:
    print(f'{city1}{city2} both citys are prasent in bangladesh')
else:
    print('the both citys are not belongs to same country')


2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
    1. Ask user to enter his fasting sugar level
    2. If it is below 80 to 100 range then print that sugar is low
    3. If it is above 100 then print that it is high otherwise print that it is normal

sugar=int(input(' enter his fasting sugar level '))
if sugar<80:
  print('the sugar is low')
elif sugar>100:
  print('the sugar is low')
elif sugar<100:
  print('sugar is high ')
else:
  print('the sugar is normal')  


[Solution - Exercise 1.i](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_1.py)

[Solution - Exercise 1.ii](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_2.py)

[Solution - Exercise 2](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise2.py)
