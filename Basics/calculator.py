def operate(a, b, choice):
    #creating a dictionary (equivalent to switch-case statements)
    switcher = { 
        1: a+b, 
        2: a-b, 
        3: a*b,
        4: a/b,
        5: a**b,
        6: a%b
    } 
    
    return switcher.get(choice, "Invalid choice")

if __name__ == '__main__':
    #Menu - Available choices
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Modulo\n")
    
    firstNum = float(input('Enter first number : '))
    secondNum = float(input('Enter second number : '))
    choice = int(input('Enter choice from the above list : '))
    
    print(operate(firstNum, secondNum, choice))
            
    
