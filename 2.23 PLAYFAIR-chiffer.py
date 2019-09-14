def get_digraphs(msg):
    digraphs = []

    while len(msg) >= 2:
        digraphs.append(msg[:2])
        msg = msg[2:]
    if len(msg) == 1:
        digraphs.append(msg)
    return digraphs


def generate_digraphs(msg):
    msg = msg.upper()
    msg = msg.replace('J', 'I').replace(' ', '')
    digraphs = []
    while True:
        digraphs = get_digraphs(msg)
        for idx, d in enumerate(digraphs):
            if len(d) > 1 and d[0] == d[1]:
                msg = msg[:idx * 2 + 1] + 'X' + msg[idx*2 + 1:]
                break
        new_digraphs = get_digraphs(msg)
        if new_digraphs == digraphs:
            break
    if len(digraphs[len(digraphs) - 1]) == 1:
        digraphs[len(digraphs) - 1] += 'X'
    return digraphs


def generate_key(key):
    table = []
    key = key.upper().replace('J', 'I').replace(' ', '')
    letter = 'A'
    used = []
    for i in range(5):
        table.append([])
        for j in range(5):
            while True:
                if len(key) > 0:
                    if key[0] not in used:
                        table[i].append(key[0])
                        used.append(key[0])
                        key = key[1:]
                        break
                    key = key[1:]
                else:
                    if letter not in used and letter != 'J':
                        table[i].append(letter)
                        used.append(letter)
                        break
                    letter = chr(ord(letter) + 1)
    return table


def encode(msg, key):
    encoded_msg = ''
    for digraph in msg:
        r_1, c_1, r_2, c_2 = -1, -1, -1, -1
        d_1, d_2 = '', ''
        if digraph == 'XX':
            encoded_msg += 'YY'
            continue
        for i in range(5):
            for j in range(5):
                if key[i][j] == digraph[0]:
                    r_1 = i
                    c_1 = j
                if key[i][j] == digraph[1]:
                    r_2 = i
                    c_2 = j
                if c_1 != -1 and c_2 != -1:
                    break
            if c_1 != -1 and c_2 != -1:
                break
        if r_1 != r_2 and c_1 != c_2:
            d_1 = key[r_1][c_2]
            d_2 = key[r_2][c_1]
        elif r_1 == r_2:
            d_1 = key[r_1][(c_1 + 1) % 5]
            d_2 = key[r_2][(c_2 + 1) % 5]
        elif c_1 == c_2:
            d_1 = key[(r_1 + 1) % 5][c_1]
            d_2 = key[(r_2 + 1) % 5][c_2]

        encoded_msg += d_1 + d_2
    return encoded_msg


def encrypt(msg, key):
    digraphs = generate_digraphs(msg)
    table = generate_key(key)
    encoded_msg = encode(digraphs, table)
    return encoded_msg


while True:
    cases = int(input())
    if cases == 0:
        break
    key = input()
    for i in range(cases):
        msg = input()
        print(encrypt(msg, key))
    print()
