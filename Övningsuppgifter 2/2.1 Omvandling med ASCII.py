def small_to_big_char(c):
    c_num = ord(c)
    if 97 <= c_num <= 122:
        return chr(c_num - 32)
    else:
        return c


print(small_to_big_char('a'))
print(small_to_big_char('x'))
print(small_to_big_char('G'))
print(small_to_big_char('_'))
print(small_to_big_char('*'))
