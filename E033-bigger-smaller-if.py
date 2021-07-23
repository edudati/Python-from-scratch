""" Return the bigger and the smaller numbers of 3 numbers"""

a = int(input('1st number: '))
b = int(input('2nd number: '))
c = int(input('3rd number: '))
smaller = a
bigger = a
if b < a and b < c:
    smaller = b
if c < b and c < a:
    smaller = c
if b > a and b > c:
    bigger = b
if c > a and c > b:
    bigger = c
print('Bigger: ', bigger)
print('Smaller: ', smaller)
