def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_series(n):
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
