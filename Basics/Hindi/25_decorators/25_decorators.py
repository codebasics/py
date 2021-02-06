def check(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not a non-negative integer")

    return helper


@check
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(1, 10):
    print(i, factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    e.print_exception()

try:
    print(factorial(1.354))
except Exception as e:
    e.print_exception()