def fib():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first+second
for f in fib():
    if f > 100:
        break
    print(f)
