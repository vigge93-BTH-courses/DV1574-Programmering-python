def introduce(name="unknown", age=None):
    res = 'My name is {}.'.format(name)
    if age is not None:
        res += ' I am {} years old.'.format(age)
    else:
        res += ' My age is a secret.'
    print(res)


introduce('Linn', 19)
introduce('Carina')
introduce()
