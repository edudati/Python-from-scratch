""" Conclude if we can make a triangle with this lines considering:
one side must be less than the sum of the other 2 sides"""

l1 = float(input('Line 1: '))
l2 = float(input('Line 2: '))
l3 = float(input('Line 3: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    print('It is possible.')
else:
    print('It is not possible.')