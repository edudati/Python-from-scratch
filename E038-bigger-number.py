""" Compare 2 numbers and return the bigger"""
n1 = int(input('1st number: '))
n2 = int(input('2nd number: '))
if n1 > n2:
    print('The number {} is bigger.'.format(n1))
elif n1 < n2:
    print('The number {} is bigger.'.format(n2))
else:
    print('The numbers are the same.')