""" Retur if the number is even or odd"""

n = int(input('Type a number: '))
par = n % 2
"""the rest of the division from 2 to even number is always zero"""

if par == 0:
    print('Even')
else:
    print('Odd')
