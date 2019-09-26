import random
import copy
from functools import reduce


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
    tree = {}
    for i in range(10):
        tree[i] = {}
        for j in range(10):
            tree[i][j] = {}
            for k in range(10):
                tree[i][j][k] = {}
                for m in range(10):
                    tree[i][j][k][m] = {'active': True}
    return tree


def get_guess(available_guesses):
    # Return [1, 1, 2, 2] at the start
    if 1 in available_guesses:
        if 1 in available_guesses[1]:
            if 2 in available_guesses[1][1]:
                if 2 in available_guesses[1][1][2]:
                    return [1, 1, 2, 2]

    # Return the code with the largest branch (No look ahead)
    guess = []
    tree = available_guesses
    for i in range(4):
        max_tree = -1
        len_max = -1
        for key in tree:
            if deep_len(tree[key]) > len_max:
                max_tree = key
                len_max = deep_len(tree[key])
        guess.append(max_tree)
        tree = tree[max_tree]
    return guess


def deep_len(tree):
    if type(tree) == bool:
        return 1
    tot = 0
    for k in tree:
        tot += deep_len(tree[k])
    return tot


def update_guesses(available_guesses, guess, correct, wrong_place, p_guess, p_correct, p_wrong_place):
    total = correct + wrong_place
    if p_guess is not None:
        p_total = p_correct + p_wrong_place
        diff = [0, 0, 0, 0]
        for i in range(len(guess)):
            diff[i] = abs(guess[i] - p_guess[i])
        num_diff = reduce(lambda x, y: x + y,
                          map(lambda x: 1 if x != 0 else 0, diff))
    del available_guesses[guess[0]][guess[1]][guess[2]][guess[3]]
    # If no numbers were in the correct position, remove all branches with this order
    if correct == 0:
        del available_guesses[guess[0]]
        for k_1 in available_guesses:
            if guess[1] in available_guesses[k_1]:
                del available_guesses[k_1][guess[1]]
            for k_2 in available_guesses[k_1]:
                if guess[2] in available_guesses[k_1][k_2]:
                    del available_guesses[k_1][k_2][guess[2]]
                for k_3 in available_guesses[k_1][k_2]:
                    if guess[3] in available_guesses[k_1][k_2][k_3]:
                        del available_guesses[k_1][k_2][k_3][guess[3]]

    tree = copy.deepcopy(available_guesses)
    # If none of the numbers are correct, delete all combination containing those numbers
    if total == 0:
        for k_1 in available_guesses:
            if k_1 in guess:
                del tree[k_1]
            else:
                for k_2 in available_guesses[k_1]:
                    if k_2 in guess:
                        del tree[k_1][k_2]
                    else:
                        for k_3 in available_guesses[k_1][k_2]:
                            if k_3 in guess:
                                del tree[k_1][k_2][k_3]
                            else:
                                for k_4 in available_guesses[k_1][k_2][k_3]:
                                    if k_4 in guess:
                                        del tree[k_1][k_2][k_3][k_4]
    # If all numbers are in the code, delete all combinations not containing those numbers
    elif total == 4:
        for k_1 in available_guesses:
            if k_1 not in guess:
                del tree[k_1]
            else:
                for k_2 in available_guesses[k_1]:
                    if k_2 not in guess:
                        del tree[k_1][k_2]
                    else:
                        for k_3 in available_guesses[k_1][k_2]:
                            if k_3 not in guess:
                                del tree[k_1][k_2][k_3]
                            else:
                                for k_4 in available_guesses[k_1][k_2][k_3]:
                                    if k_4 not in guess:
                                        del tree[k_1][k_2][k_3][k_4]
    available_guesses = tree
    clean_tree(available_guesses)
    return available_guesses


def clean_tree(tree_in):
    if type(tree_in) == bool:
        return False
    if len(tree_in) == 0:
        return True
    else:
        tree = copy.deepcopy(tree_in)
        for k in tree_in:
            if clean_tree(tree[k]):
                del tree[k]
        keys = list(tree_in.keys())
        for k in keys:
            if not k in tree:
                del tree_in[k]
            else:
                tree_in[k] = tree[k]
        if len(tree) == 0:
            return True
        return False

# def get_combinations():
#     combinations = []
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 for m in range(10):
#                     combinations.append(f'{i}{j}{k}{m}')
#     combinations = [list(x) for x in combinations]
#     return combinations


# def get_guess(available_guesses):
#     """Uses Knuths 5-step algorithm to find next guess\n
#     https://en.wikipedia.org/wiki/Mastermind_(board_game)#Five-guess_algorithm
#     """
#     guess = []
#     if ['1', '1', '2', '2'] in available_guesses:
#         guess = ['1', '1', '2', '2']
#     else:
#         guess = available_guesses[random.randint(
#             0, len(available_guesses) - 1)]
#     return [int(g) for g in guess]


# def update_guesses(available_guesses, guess, correct, wrong_place):
#     guess = [str(g) for g in guess]
#     available_guesses.remove(guess)
#     guess_dict = {}
#     total = correct + wrong_place
#     # Create a dict of guess
#     for g in guess:
#         if g in guess_dict:
#             guess_dict[g] += 1
#         else:
#             guess_dict[g] = 1
#     res_arr = available_guesses[:]

#     # Remove all guesses where the occurence of one digit is greater than the total correct.
#     for key in guess_dict:
#         if guess.count(key) > total:
#             for a_g in available_guesses:
#                 if a_g.count(key) > total:
#                     res_arr.remove(a_g)
#         available_guesses = res_arr[:]

#     # Removed based on number of unique guesses
#     if len(guess_dict) == 1:
#         for g in guess_dict:
#             for a_g in available_guesses:
#                 if a_g.count(g) < total:
#                     res_arr.remove(a_g)
#             available_guesses = res_arr[:]

#     elif len(guess_dict) == 2:
#         if guess_dict[list(guess_dict.keys())[0]] == 2 and total == 3:
#             for g in guess_dict:
#                 for a_g in available_guesses:
#                     if a_g.count(g) < 1:
#                         res_arr.remove(a_g)
#                 available_guesses = res_arr[:]
#         elif total == 3:
#             for g in guess_dict:
#                 if guess_dict[g] == 3:
#                     for a_g in available_guesses:
#                         if a_g.count(g) < 2:
#                             res_arr.remove(a_g)
#                     available_guesses = res_arr[:]
#         elif total == 4:
#             for g in guess_dict:
#                 for a_g in available_guesses:
#                     if guess_dict[g] != a_g.count(g):
#                         res_arr.remove(a_g)
#                 available_guesses = res_arr[:]
#     elif len(guess_dict) == 3:
#         if total == 3:
#             for g in guess_dict:
#                 if guess_dict[g] == 2:
#                     for a_g in available_guesses:
#                         if a_g.count(g) < 1:
#                             res_arr.remove(a_g)
#                     available_guesses = res_arr[:]

#     # Removed based on number correct
#     for a_g in available_guesses:
#         num_keys = 0
#         for g in guess_dict:
#             if g in a_g:
#                 num_keys += min(guess_dict[g], a_g.count(g))
#         if num_keys < total:
#             res_arr.remove(a_g)
#     available_guesses = res_arr[:]
#     return available_guesses


ROWS = 500
CODE_LEN = 4


welcome_str = 'Welcome to the ”Master Mind”'
print(welcome_str)
print(''.center(len(welcome_str), '-'))

available_guesses = get_combinations()
code = generate_code()
guesses = 0
last_guess = None
last_correct = 0
last_wrong_place = 0
while guesses < ROWS:
    guess = print('Guess my secret code (4 numbers 0-9): ', end='')
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
    print(*nums)
    guesses += 1

    correct = get_numbers_correct(nums, code)
    wrong_place = get_numbers_wrong_place(nums, code)

    available_guesses = update_guesses(
        available_guesses, nums, correct, wrong_place, last_guess, last_correct, last_wrong_place)
    last_guess = nums
    last_correct = correct
    last_wrong_place = wrong_place
    if correct == CODE_LEN:
        print(f'Congratulations, you succeeded in {guesses} guesses')
        break
    else:
        print(
            f'Your guess had {correct} numbers in correct position and {wrong_place} in wrong position.\n')

if guesses == ROWS:
    print(f'Haha you lost, loser. The code was {code}')
