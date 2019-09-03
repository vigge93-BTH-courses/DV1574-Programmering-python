def unit(n):
    """
    Returns the digit in the units place

    Keyword arguments:
    n -- The number to process
    """
    return n % 10


def ten(n):
    """
    Returns the digit in the tens place

    Keyword arguments:
    n -- The number to process
    """
    return (n // 10) % 10


def digit(num, n):
    """
    Returns the digit in the specified place

    Keyword arguments:
    num -- Number to process
    n -- Position to extract the number, counted right to left starting at 1.
    """
    return (num // 10 ** (n-1)) % 10


print(unit(123))
print(ten(123))
print(digit(1234, 2))
print(digit(1234, 4))
