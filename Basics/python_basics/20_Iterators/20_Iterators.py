class fibonacci:
    def __init__(self):
        # default constructor
        self.previous = 0
        self.current = 1
        self.n = 1

    def __iter__(self):  
        return self

    def __next__(self): 
        if self.n < 5: 
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration  

# init the fib_iterator
fib_iterator = iter(fibonacci())
while True:
    # print the value of next fibonaccinacci up to 5th fibonaccinacci
    try:
        print(next(fib_iterator))
    except StopIteration:
        break  


