
country = {'china': 143, 'india':136,'usa': 32,'pakistan':21}
name = input('abcd: ')


if name == 'a':
    for i in country:
        print(i,'==>',country[i])

elif name == 'b':
    country_name = input('Country name:')
    if country_name in country:
        print('This country have in list')
    else:
        country_population = input('country population: ')
        country[country_name] = int(country_population)
        print(country)
elif name == 'c':
    country_delete = input('How country you want delete? ')
    if country_delete in country:
        del country[country_delete]
        for i in country:
            print(i, '==>', country[i])
    else:
        print('Not have this country')
elif name == 'd':
    country_pop = input('how you want know country population? ')
    if country_pop in country:
        print(country[country_pop])
