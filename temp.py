# # def increment_5(seq):
# #     if not seq:
# #         return []
# #     return [seq[0] + 5] + increment_5(seq[1:])


# # def first_elements(seq):
# #     if not seq:
# #         return []
# #     return [seq[0][0]] + first_elements(seq[1:])


# def with_all(func, seq):
#     '''Applies func to the sequence.'''
#     if not seq:
#         return []
#     return [func(seq[0])] + with_all(func, seq[1:])


# def increment_5(seq):
#     '''_'''
#     return with_all(lambda n: n + 5, seq)

# def increment_5(seq):
#     '''_'''
#     return [n + 5 for n in seq]


# def first_elements(seq):
#     '''_'''
#     return with_all(lambda seq: seq[0], seq)

# def first_elements(seq):
#     '''_'''
#     return [lst[0] for lst in seq]

# print(*increment_5([10, 20, 30]), sep=', ')
# print(*first_elements([[1, 2, 3], ['q', 'd', 'b'],
#                        ['Helloo', 'there']]), sep=', ')

def modulus_raknare(steps):
    """Returns a circular counting function."""
    i = 0

    def next_step():
        nonlocal i
        i = (i + 1) % steps
        return i
    return next_step
