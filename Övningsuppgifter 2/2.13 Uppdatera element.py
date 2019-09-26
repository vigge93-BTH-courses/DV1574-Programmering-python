

start_list = [5, 3, 1, 2, 4]
square_list = []

square_list = sorted(map((lambda x: x ** 2), start_list))
print(*square_list)
