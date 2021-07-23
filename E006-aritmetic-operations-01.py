# Some aritmetic operations using variables

import math
x = int(input('Type any number: '))

d = x * 2
t = x * 3
sq = x ** (1/2)
sqFromLibrary = math.sqrt(x)
'''line above not used, just for exercise'''

print('The number is {}, the double is {}, the triple is {}, the square root is {}'.format(x, d, t, sq))