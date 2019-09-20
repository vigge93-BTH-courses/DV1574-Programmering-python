import random


def generate_code():
    return [random.randint(0, 9) for x in range(CODE_LEN)]


def get_numbers_correct(nums, code):
    tot = 0
    for i in range(CODE_LEN):
        if nums[i] == code[i]:
            tot += 1
    return tot


def get_correct_numbers(nums, code):
    res = []
    for i in range(CODE_LEN):
        if nums[i] == code[i]:
            res.append(nums[i])
    return res


def get_numbers_wrong_place(nums, code):
    code = code[:]
    nums = nums[:]
    correct = get_correct_numbers(nums, code)
    for i in correct:
        nums.remove(i)
        code.remove(i)
    tot = 0
    for i in range(len(nums)):
        for j in range(len(code)):
            if i == j:
                continue
            if nums[i] == code[j]:
                tot += 1
                break
    return tot


ROWS = 12
CODE_LEN = 4

welcome_str = 'Welcome to the ”Master Mind”'
print(welcome_str)
print(''.center(len(welcome_str), '-'))


code = generate_code()
guesses = 0
while guesses < ROWS:
    guess = input('Guess my secret code (4 numbers 0-9): ')
    nums = guess.split()
    if len(nums) != CODE_LEN:
        print('Invalid guess, try again.')
        continue

    try:
        nums = [int(x) for x in nums]
        if max(nums) > 9 or min(nums) < 1:
            raise ValueError
    except ValueError:
        print('Invalid guess, try again.')
        continue

    guesses += 1

    correct = get_numbers_correct(nums, code)
    wrong_place = get_numbers_wrong_place(nums, code)
    if correct == CODE_LEN:
        print(f'Congratulations, you succeeded in {guesses} guesses')
        break
    else:
        print(
            f'Your guess had {correct} numbers in correct position and \
                {wrong_place} in wrong position\n')

if guesses == ROWS:
    print('Haha you lost, loser.')
