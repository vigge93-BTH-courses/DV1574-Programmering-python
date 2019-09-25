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
        j = 0
        while j < len(code):
            if nums[i] == code[j]:
                code.pop(j)
                tot += 1
                break
            j += 1
    return tot


def get_combinations():
    combinations = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for m in range(10):
                    combinations.append(f'{i}{j}{k}{m}')
    combinations = [list(x) for x in combinations]
    return combinations


def get_guess(available_guesses):
    """Uses Knuths 5-step algorithm to find next guess\n
    https://en.wikipedia.org/wiki/Mastermind_(board_game)#Five-guess_algorithm
    """
    guess = []
    if ['1', '1', '2', '2'] in available_guesses:
        guess = ['1', '1', '2', '2']
    else:
        guess = available_guesses[random.randint(
            0, len(available_guesses) - 1)]
    return [int(g) for g in guess]


def update_guesses(available_guesses, guess, correct, wrong_place):
    guess = [str(g) for g in guess]
    available_guesses.remove(guess)
    guess_dict = {}
    total = correct + wrong_place
    # Create a dict of guess
    for g in guess:
        if g in guess_dict:
            guess_dict[g] += 1
        else:
            guess_dict[g] = 1
    res_arr = available_guesses[:]

    # Remove all guesses where the occurence of one digit is greater than the total correct.
    for key in guess_dict:
        if guess.count(key) > total:
            for a_g in available_guesses:
                if a_g.count(key) > total:
                    res_arr.remove(a_g)
        available_guesses = res_arr[:]

    # Removed based on number of unique guesses
    if len(guess_dict) == 1:
        for g in guess_dict:
            for a_g in available_guesses:
                if a_g.count(g) < total:
                    res_arr.remove(a_g)
            available_guesses = res_arr[:]

    elif len(guess_dict) == 2:
        if guess_dict[list(guess_dict.keys())[0]] == 2 and total == 3:
            for g in guess_dict:
                for a_g in available_guesses:
                    if a_g.count(g) < 1:
                        res_arr.remove(a_g)
                available_guesses = res_arr[:]
        elif total == 3:
            for g in guess_dict:
                if guess_dict[g] == 3:
                    for a_g in available_guesses:
                        if a_g.count(g) < 2:
                            res_arr.remove(a_g)
                    available_guesses = res_arr[:]
        elif total == 4:
            for g in guess_dict:
                for a_g in available_guesses:
                    if guess_dict[g] != a_g.count(g):
                        res_arr.remove(a_g)
                available_guesses = res_arr[:]
    elif len(guess_dict) == 3:
        if total == 3:
            for g in guess_dict:
                if guess_dict[g] == 2:
                    for a_g in available_guesses:
                        if a_g.count(g) < 1:
                            res_arr.remove(a_g)
                    available_guesses = res_arr[:]

    # Removed based on number correct
    for a_g in available_guesses:
        num_keys = 0
        for g in guess_dict:
            if g in a_g:
                num_keys += min(guess_dict[g], a_g.count(g))
        if num_keys < total:
            res_arr.remove(a_g)
    available_guesses = res_arr[:]
    return available_guesses


ROWS = 500
CODE_LEN = 4


def main():
    #welcome_str = 'Welcome to the ”Master Mind”'
    # print(welcome_str)
    #print(''.center(len(welcome_str), '-'))

    available_guesses = get_combinations()
    code = generate_code()
    guesses = 0
    while guesses < ROWS:
        #guess = print('Guess my secret code (4 numbers 0-9): ', end='')
        # nums = guess.split()
        # if len(nums) != CODE_LEN:
        #     print('Invalid guess, try again.')
        #     continue

        # try:
        #     nums = [int(x) for x in nums]
        #     if max(nums) > 9 or min(nums) < 1:
        #         raise ValueError
        # except ValueError:
        #     print('Invalid guess, try again.')
        #     continue

        nums = get_guess(available_guesses)
        # print(*nums)
        guesses += 1

        correct = get_numbers_correct(nums, code)
        wrong_place = get_numbers_wrong_place(nums, code)

        available_guesses = update_guesses(
            available_guesses, nums, correct, wrong_place)
        if correct == CODE_LEN:
            #print(f'Congratulations, you succeeded in {guesses} guesses')
            break
        else:
            pass
            # print(
            #    f'Your guess had {correct} numbers in correct position and {wrong_place} in wrong position.\n')

    if guesses == ROWS:
        pass
        #print(f'Haha you lost, loser. The code was {code}')
    return guesses


tot = 0
ite = 1000
for i in range(ite):
    print(i)
    tot += main()

print('Avg tries: ' + str(tot/ite))
