## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
Kazakhstan = ['Astana','Shymkent','Almaty','Aktau','Oral']
America = ['New-York','Washington','Texas']
Russia = ['Moscow','Sankt-peterburgs','Omsk','Chelyabinsk']

city = input('enter your city:')
city1 = input('Enter your city 2')
if city in Kazakhstan and city1 in Kazakhstan:
    print('Kazakhstan')
elif city in America and city1 in America:
    print('America')
elif city in Russia and city1 in Russia:
    print('Russia')
else:
    print('they dont belong to same country', city)
