import numbers
from functools import reduce


def get_value(el):
    if isinstance(el, numbers.Number):
        return el
    else:
        return 0


def sum_numbers(any_list):
    return reduce(lambda x, y: get_value(x) + get_value(y), any_list)


print(sum_numbers([1, 2, 3.2, 4, 5]))
print(sum_numbers(['a', 1, 'b', 2, [['b', 4], 2], 3]))
