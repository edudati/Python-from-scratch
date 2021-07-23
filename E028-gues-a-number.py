"""Guess a number from 1 to 5"""

import random

n = int(input('Guess a number from 1 to 5: '))
selected = random.randint(1, 5)

if n < 1 or n > 5:
    print('The number is out of the options.')
if n == selected:
    print('Congrats, you got it right!!!')
else:
    print('Sorry, I thought about the number {} and you selected {}.'.format(selected, n))
