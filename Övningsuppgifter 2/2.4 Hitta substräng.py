

def search(string, substring):
    for i, c in enumerate(string):
        if c == substring[0]:
            if string[i:i + len(substring)] == substring:
                return i
    return -1


print(search('elephant', 'ant'))
print(search('apple', 'p'))
print(search('Giraff', 'Aff'))
