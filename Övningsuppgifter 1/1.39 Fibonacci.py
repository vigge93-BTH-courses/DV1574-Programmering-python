def fib(n):
    """
    Recursively calculate Fib(n).

    Calculates the value for the n:th term in the fibonacci sequence defined.
    by the following:\n
    a_0 = 0\n
    a_1 = 1\n
    a_n = a_(n-1) + a_(n-2)

    Keyword arguments:
    n -- Position to calculate
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_series(n):
    """
    Print n numbers in the fibonacci sequence.

    Keyword arguments:
    n -- number of values to calculate
    """
    for i in range(n+1):
        print(fib(i))


print(fib(0))
print('')
print(fib(1))
print('')
fib_series(1)
print('')
print(fib(2))
print('')
fib_series(2)
print('')
print(fib(3))
print('')
fib_series(3)
print('')
print(fib(4))
print('')
fib_series(4)
print('')
print(fib(5))
print('')
fib_series(5)
print('')
print(fib(6))
print('')
fib_series(6)
