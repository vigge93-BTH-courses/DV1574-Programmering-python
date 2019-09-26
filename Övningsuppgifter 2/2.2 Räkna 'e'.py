def count_e(word):
    tot = 0
    for c in word:
        if c == 'e':
            tot += 1
    return tot


print(count_e('elephant'))
print(count_e('Egg'))
print(count_e('interference'))
