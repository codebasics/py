variables
=========
>>> first="Tom"
>>> middle="Cruise"
>>> last="Mapother"
>>> print("Full Name:",first,middle,last)
Full Name: Tom Cruise Mapother

numbers
=======
(1) Find out an area of a triangle whose base is 15 meter and height is 22 meter. The mathematical equation for an area of a triangle is: Area = ½*Base*Height
>>> base=15
>>> height=22
>>> area=1/2*(base*height)
>>> area
165.0

(2) You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back? 
>>> num_packets=9
>>> cost_per_packet=1.49
>>> total_cost=num_packets*cost_per_packet
>>> money_paid=20
>>> cash_back=money_paid-total_cost
>>> cash_back
6.59

(3) The bathroom of your home is an exact square. You want to replace tiles in it. Length of this bathroom is 5.5 feet. How many square foot of tiles you need to buy? Equation for an area of a square is: Area = Length to the power of 2. Find it out using python.
>>> length=5.5
>>> area=length**2
>>> area
30.25

strings
=======
(1) Create a string variable to store this text "Earth revolves around the sun",
    (a) Print substring “revolves” 
    (b) Print substring “sun” using negative index
>>> s="Earth revolves around the sun"
>>> s[6:14]
'revolves'
>>> s[-3:]
'sun'
(2) Create a string variable to store this text "Earth revolves around the “sun”" and print it
>>> s='Earth revolves around the “sun”'
>>> s
'Earth revolves around the “sun”'
(3) Create three string variables with values “I love eating“, “veggies”, “fruits” 
    (a) Print “I love eating veggies and fruits” (Hint: Use + operator)
>>> s1="I love eating"
>>> s2="veggies"
>>> s3="fruits"
>>> s1+" " +s2+" and "+s3
'I love eating veggies and fruits'
    (b) Create fourth variable to store number of fruits you eat everyday. Say for example you eat 2 fruits everyday, in that case print “I love eating 2 fruits everyday”
>>> num_fruits=2
>>> s1+" "+str(num_fruits)+" "+s3+" everyday"
'I love eating 2 fruits everyday'
