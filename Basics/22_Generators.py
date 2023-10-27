def gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
for i in fib():
    if i > 100:
        break
    print(i)
