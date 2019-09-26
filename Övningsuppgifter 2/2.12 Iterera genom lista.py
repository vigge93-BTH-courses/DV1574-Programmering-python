from functools import reduce


def add_numbers_in_list(num_list):
    return reduce((lambda x, n: x + n), num_list, 0)


print(add_numbers_in_list([]))
print(add_numbers_in_list([10, 20, 30]))
print(add_numbers_in_list([-10, -20, 30]))
