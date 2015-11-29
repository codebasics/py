
def break_demo():
    """Demonstrate use of break by taking expense as input and print
    month in which that expense occurred. Break whenever appropriate
    month is found"""

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


def break_demo_run():
    """break demo using running race"""
    for i in range(26):
        print("You ran",i+1,"miles.") # i starts with zero hence adding 1
        tired = input("Are you tired?")
        if tired == 'yes':
            break

    if i==26:
        print("Hurray! You are a star. You just finished marathon!")
    else:
        print("Total miles ran",i+1)
        print("You didn't finish marathon but congrats anyways!")

break_demo_run()

