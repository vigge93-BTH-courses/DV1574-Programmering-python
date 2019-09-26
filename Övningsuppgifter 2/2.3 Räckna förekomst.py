def count_char(string, char):
    tot = 0
    for c in string:
        if c == char:
            tot += 1
    return tot


print(count_char('elephant', 'e'))
print(count_char('Lion', 'i'))
print(count_char('Giraffe', 'g'))
