def unit(n):
    return n % 10


def ten(n):
    return (n // 10) % 10


def swap_units_and_ten(n):
    arr_n = [c for c in str(n)]
    arr_n[len(arr_n) - 1] = str(ten(n))
    arr_n[len(arr_n) - 2] = str(unit(n))
    res = ''.join(arr_n)
    return(res)


print(swap_units_and_ten(123))
