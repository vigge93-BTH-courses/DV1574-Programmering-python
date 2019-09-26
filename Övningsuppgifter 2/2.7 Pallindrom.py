
while True:
    word = input('Write a word: ')
    if word == 'quit':
        print('Exiting ...')
        break

    if word[::-1].lower() == word.lower():
        print(word, 'is a palindrome')
    else:
        print(word, 'is not a palindrome')
    print()
