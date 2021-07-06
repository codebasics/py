# Exercise
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
length=92
width=48.8
area=length*width
print("area of football field:",area) # Ans: 4489.599999999999

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
num_packets=9
cost_per_packet=1.49
total_cost=num_packets*cost_per_packet
money_paid=20
cash_back=money_paid-total_cost
print("Cash back:",cash_back) # Ans: 6.59

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
length=5.5
area=length**2 # area of square is length power 2
cost=area*500
print("total cost for bathroom tiles replacement:",cost) # Ans: 15125.0

# 4. Print binary representation of number 17
num=17
print('Binary of number 17 is:',format(num,'b')) # Ans: 10001