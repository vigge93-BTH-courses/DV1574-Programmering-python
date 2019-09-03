def original(n):
    if n > 10:
        if n > 100:
            if n < 1000:
                print(n)
            else:
                if n < 1001:
                    print('Pretty large')
                else:
                    print(n)
        else:
            if n == 11:
                print(n)
            else:
                if n == 10:
                    print('10!')
                else:
                    print(n)
    else:
        if n < 0:
            print('Below zero')
        else:
            print(n)


def new(n):
    if n < 0:
        print('Below zero')
    elif n == 1000:
        print('Pretty large')
    else:
        print(n)
