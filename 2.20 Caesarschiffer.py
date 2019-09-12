def encrypt(msg, key):
    msg = msg.upper()
    res = ''
    for c in msg:
        if 65 <= ord(c) <= 90:
            res += chr(((ord(c)-65 + key) % 26) + 65)
        else:
            res += c
    return res


def decrypt(msg, key):
    msg = msg.upper()
    res = ''
    for c in msg:
        if 65 <= ord(c) <= 90:
            res += chr(((ord(c)-65 - key) % 26) + 65)
        else:
            res += c
    return res


print(encrypt('Vi anfaller tidigt imorgon!', 5))
print(encrypt('Bruce Wayne är Batman!', 17))
print(decrypt('SILTV NRPEV ÄI SRKDRE!', 17))
