full = {
    'info' :[600, 630, 620],
    'ril' : [1430, 1490, 1567],
    'mtl' : [234, 180, 160]
}

def full_list():
    for key, i in full.items():
        print(f"{key}==>{i}")

def add_list():
    stock = input('stock')
    price = (int(input('price')))
    if stock in full:
        full[stock].append(price)
    else:
        full[stock] = [price]
    full_list()

def main ():
    op = input('take operation :(print,add or amend?)')
    if op.lower() == 'print':
        full_list()
    elif op.lower() == 'add':
        add_list()
    else:
        print('Unsupported operation:', op)

if __name__ == '__main__':
    main()
