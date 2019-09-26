def BMI(w, h):
    """
    Calculates BMI.

    Keyword arguments:
    w -- width
    h -- height
    """
    return round(w / (h ** 2), 2)


print(BMI(63, 1.70))
print(BMI(110, 2.00))
