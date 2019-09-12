def generate_diagraphs(msg):
    diagraphs = []
    for c in range(0, len(msg), 2):
        diagraphs.append([msg[c], msg[c+1]])
    return diagraphs


def encrypt(msg, key):
    msg = msg.upper()
    msg.replace('J', 'I')
    diagraphs = []
    while True:
        diagraphs = generate_diagraphs(msg)
        for idx, d in enumerate(diagraphs):
            if d[0] == d[1]:
                msg = msg[:idx * 2 + 1] + 'X' + msg[idx*2 + 1:]
                break
        new_diagraphs = generate_diagraphs(msg)
        if new_diagraphs == diagraphs:
            break
    if len(diagraphs[len(diagraphs) - 1]) == 1:
        diagraphs[len(diagraphs)].append('X')
    table = []
    print(diagraphs)


encrypt('Hello world', 2)
encrypt('Whops', 2)
