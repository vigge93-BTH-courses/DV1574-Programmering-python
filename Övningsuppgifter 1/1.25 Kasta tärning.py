import random

name_p1 = input('Player 1, enter your name: ')
name_p2 = input('Player 2, enter your name: ')

dice_p1 = random.randint(1, 6)
dice_p2 = random.randint(1, 6)

print('{}, your dice shows {}'.format(name_p1, dice_p1))
print('{}, your dice shows {}'.format(name_p2, dice_p2))
print('Winner is {}!'.format(name_p1 if dice_p1 > dice_p2 else
                             name_p2 if dice_p2 > dice_p1 else
                             'both'))
