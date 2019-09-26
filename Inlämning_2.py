import random


def generate_code():
    '''Generates and returns a list with the code.'''
    return [random.randint(MIN_VALUE, MAX_VALUE + 1) for x in range(CODE_LEN)]


def get_numbers_correct(guess, code):
    '''Returns the number of numbers that were correctly placed.'''
    total = 0
    for idx in range(CODE_LEN):
        if guess[idx] == code[idx]:
            total += 1
    return total


def get_correct_numbers(guess, code):
    '''Returns the numbers that were correctly placed.'''
    result = []
    for idx in range(CODE_LEN):
        if guess[idx] == code[idx]:
            result.append(guess[idx])
    return result


def get_numbers_wrong_place(guess, code):
    '''Returns the number of numbers that are in the code,
    but in the wrong place.'''
    code = code[:]
    guess = guess[:]
    correct = get_correct_numbers(guess, code)
    # The numbers that are in the correct place can't be in the wrong place
    for num in correct:
        guess.remove(num)
        code.remove(num)

    total = 0
    for i in range(len(guess)):
        j = 0
        # Iterate through the code until a match is found or end is reached
        # Then continue to the next number in the guess
        while j < len(code):
            if guess[i] == code[j]:
                code.pop(j)
                total += 1
                break
            j += 1
    return total


def validate_guess(guess):
    '''Converts the guess to integers and returns True if it is valid.'''
    guess_valid = True
    if len(guess) != CODE_LEN:
        guess_valid = False
    else:
        try:
            for idx, value in enumerate(guess):
                guess[idx] = int(value)
            if max(guess) > MAX_VALUE or min(guess) < MIN_VALUE:
                raise ValueError
        except ValueError:
            guess_valid = False
    return guess_valid


CODE_LEN = 4
MIN_VALUE = 0
MAX_VALUE = 9

welcome_str = 'Welcome to the ”Master Mind”.'
print(welcome_str)
print(''.center(len(welcome_str), '-'))

code = generate_code()
guesses = 0
has_won = False
while not has_won:
    guess = input('Guess my secret code (4 numbers 0-9): ')
    guess = guess.split()

    if validate_guess(guess):
        guesses += 1

        correct = get_numbers_correct(guess, code)
        wrong_place = get_numbers_wrong_place(guess, code)

        if correct == CODE_LEN:
            print(f'Congratulations, you succeeded in {guesses} guesses.')
            has_won = True
        else:
            print(f'Your guess had {correct} numbers in the correct position and \
{wrong_place} numbers in the wrong position.\n')
    else:
        print('Invalid guess, try again.')
