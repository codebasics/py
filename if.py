def city_checker():
    '''if chapter exercise (a)'''

    usa = ["atlanta", "new york", "chicago", "baltimore"]
    uk = ["london", "bristol", "cambridge"]
    india = ["mumbai", "delhi", "banglore"]

    city = input("Enter city name: ")

    if city in usa:
        print(city,"is in usa")
    elif city in uk:
        print(city,"is in uk")
    elif city in india:
        print(city,"is in india")
    else:
        print("I won't be able to tell you which country",city,"is in! Sorry!")


def city_country_checker():
    '''if chapter exercise (b)'''

    usa = ["atlanta", "new york", "chicago", "baltimore"]
    uk = ["london", "bristol", "cambridge"]
    india = ["mumbai", "delhi", "banglore"]

    city1 = input("Enter city 1: ")
    city2 = input("Enter city 2: ")

    if city1 in usa and city2 in usa:
        print("Both cities are in USA")
    elif city1 in uk and city2 in uk:
        print("Both cities are in uk")
    elif city1 in india and city2 in india:
        print("Both cities are in India")
    else:
        print("They don't belong to same country")


def cuisine_checker():
    '''If tutorial'''

    indian = ["samosa","kachori", "dal", "naan" ]
    chinese = ["egg roll", "fried rice", "pot sticker"]
    italian = ["pizza", "pasta", "risotto"]

    dish = input("Enter a dish name: ")
    if dish in indian:
        print(dish,"is an indian cuisine")
    elif dish in chinese:
        print(dish,"is a chinese cuisine")
    elif dish in italian:
        print(dish,"is an italian cuisine")
    else:
        print("Based on whatever little knowledge I've, I can't tell which cuisine is",dish)


city_checker()