# Broke a number

from math import trunc

n = float(input('type a number: '))

print('\nthe number was {} and its whole portion was {}.'.format(n, int(n)))
print('\nthe number was {} and its whole portion was {}.'.format(n, trunc(n)))