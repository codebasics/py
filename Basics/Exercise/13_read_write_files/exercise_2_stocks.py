with open('C://Users//77081//PycharmProjects//Data//stocks.csv','r') as f, open('C://Users//77081//PycharmProjects//Data//output.csv','w') as out:
    out.write('Company name, PE ratiom,PB ration\n')
    next(f)
    for line in f:
        tokens = line.split(',')
        stock = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price/eps, 2)
        pb = round(price/book, 2)
        out.write(f'{stock},{pe},{pb}\n')
