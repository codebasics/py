

# ============ Exercises =============== #
def ex_expense_break():
    """
    Your monthly expense list (from Jan to May) looks like this,
    expense_list = [2340, 2500, 2100, 3100, 2980]
    Write a program that asks you to enter an expense amount and program
    should tell you in which month that expense occurred.
    """

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
        print('You spent',e,'in',month_list[month])
    else:
        print('You didn\'t spend',e,'in any month')


def ex_print_shape():
    """
    Write a program that prints following shape
    *
    **
    ***
    ****
    *****
    """
    for i in range(1,6):
        s = ''
        for j in range(i):
            s += '*'
        print(s)


def ex_heads_tails():
    """
    After flipping a coin 10 times you got this result,
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    Using for loop figure out “heads” count.
    """
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    count = 0
    for item in result:
        if item == "heads":
            count += 1
    print("Heads count: ",count)


# ============ Demo =============== #
def demo_break_marathon():
    """break demo using running race"""
    for i in range(26):
        print("You ran",i+1,"miles.") # i starts with zero hence adding 1
        tired = input("Are you tired? ")
        if tired == 'yes':
            break

    if i == 26:
        print("Hurray! You are a rock star! You just finished marathon!")
    else:
        print("You didn't finish marathon but hey congrats anyways! You still ran", i+1,"miles")


def demo_continue():
    """Print square of all numbers between 1 to 10 except even numbers"""
    for i in range(1,11):
        if i % 2 == 0:
            continue
    print(i*i)



