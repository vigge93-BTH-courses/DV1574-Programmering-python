def pi(k):
    sum = 0
    for n in range(k):
        sum += ((-1)**n) / (2 * n + 1)
    return sum * 4


print(pi(1))
print(pi(10))
print(pi(50))
print(pi(100))
print(pi(200))
print(pi(300))
print(pi(500))
print(pi(1000))
print(pi(10000))
