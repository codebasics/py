def add_and_multiple(n1,n2):
    '''
    Exercise 2
    :param n1: Number 1
    :param n2: Number 2
    :return: a tuple containing sum and multiplication of two input numbers
    '''
    sum = n1 + n2
    mult = n1 * n2
    return sum, mult

def age_dictionary():
    '''
    Exercise 1
    This program asks for person name and age and builds a dictionary using that
    Later on you can input person name and it will tell you the age of that person
    :return:
    '''
    d = {}
    while True:
        person = input("Enter name of the person(To stop don't enter anything and hi Enter key):")
        if person == '':
            break
        age = input("Enter age:")
        d[person] = age

    print("Building dictionary is complete.Now enter name of the person and I'll tell you his/her age")
    while True:
        name = input("Enter name of the person(To stop don't enter anything and hi Enter key):")
        if name == '':
            break
        if name in d:
            print ("Age of", name, "is:", d[name])
        else:
            print ("I don't know the age of",name)
    print ("Age dictionary program is finished now")

# Exercise 1
age_dictionary()

# Exercise 2
n1=4
n2=6
s,m=add_and_multiple(n1,n2)
print("sum:",s,"multipication:",m," Input numbers:",n1,"and",n2)
