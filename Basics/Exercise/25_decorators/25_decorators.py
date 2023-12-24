def check(f):
    def helper(x):
        if type(x) == int and x >= 0: #this should be >= to include 0 as well.
            return f(x)
        else:
            raise Exception("Argument is not a non-negative integer")

    return helper


@check
def factorial(n):
    if n == 1 or n==0: #0!=1
        return 1
    else:
        return n * factorial(n - 1)


for i in range(10):
    print(i, factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    print(str(e))

try:
    print(factorial(1.354))
except Exception as e:
    print(str(e))
