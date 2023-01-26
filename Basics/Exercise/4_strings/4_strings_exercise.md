## Exercise: String in Python

1. Create 3 variables to store street, city and country, now create address variable to
store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line


X='Malkapur'
Y='Kamareddy'
Z='India'
Address=X+'\n'+Y+'\n'+Z # HERE PRINTED BY THE +AND\N METHOD 
print(Address)
''' out put = Malkapur
              kamareddy
              India'''
Adress=f'{x}\n{y}\n{z}'
print(Adress)
''' out put=Malkapur
            Kamareddy
            India'''



2. Create a variable to store the string "Earth revolves around the sun"
    1. Print "revolves" using slice operator
    2. Print "sun" using negative index

x='earth revolves around the sun'
print(x[6:14])
#Out put = revolves
print(x[-4:-1]
#output= sun


3. Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

ft='apple','banana','cherry'
veg='onion','potato','tomato'
Z=f'i eat {veg} veggies and {ft} fruits daily'
print(z)
# out put = i eat ( 'onion','potato','tomato') veggies and ('apple','banana','cherry') fruits daily




4. I have a string variable called s='maine 200 banana khaye'. This of course is a
wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string.
Also try to do this in one line.

s='maine 200 banana khaye'
x='maine 10 samosa khaye'


[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/4_strings/4_string_exercise_answer.py)
