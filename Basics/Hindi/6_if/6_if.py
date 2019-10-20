# while mentioning topics say that timeline is in video description
# so you don't need to watch entire video

n=input("Enter a number")
n=int(n)
if n%2==0:
    print("Number is even")
else:
    print("Number is odd")

	
# Show the execution by debugging
# If is called control statement as it controls the flow of code execution

# go to idle and explain different operators

# ==
# !=
# >
# <
# >=
# <=
#
# 3>2 and 4>1
# 3>1 or 4>8
# not 4==4


# Cousine checker. Explains if..elif..else
indian=["samosa","kachori","dal","naan"]
pakistani=["nihari","paya","karahi"]
bangladesi=["panta bhat","chorchori","fuchka"]

dish=input("Enter a dish name:")

if dish in indian:
    print(f"{dish} is Indian")
elif dish in pakistani:
    print(f"{dish} is pakistani")
elif dish in bangladesi:
    print(f"{dish} is bangladesi")
else:
    print(f"Based on my limited knowledge, I don't know which cuisine is {dish}")
	

# Ternary operator
print("Ternary operator demo")
n=input("Enter a number:")
n=int(n)
message="Number is even" if n%2==0 else "Number is odd"
print(message)	
