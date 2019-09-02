def original(n):
    if n > 0:
        if n > 100:
            print('Big!')
        else:
            if n <= 50:
                print('Medium')
            else:
                print('A little larger')
    else:
        print('Tiny')


def new(n):
    if n < 0:
        print('Tiny')
    elif n <= 50
    print('Medium')
    elif n <= 100:
        print('A little larger')
    else:
        print('Big!')
