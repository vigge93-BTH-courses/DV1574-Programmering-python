def hanoi(n, start, goal, temp):
    if n == 0:
        return
    hanoi(n - 1, start, temp, goal)
    print_move(start, goal)
    hanoi(n - 1, temp, goal, start)


def print_move(f, t):
    print(f'Move {f} to {t}')


hanoi(5, 'A', 'C', 'B')
