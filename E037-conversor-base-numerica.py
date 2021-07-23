""" Convert a number to other numeric bases
1- Binary
2- Octal
3- Hexadecimal """

n = int(input('Number: '))
print('Convertion option:\n1 for Binary\n2 for Octal\n3 for Hexadecimal')
b = int(input('Option: '))
if b == 1:
    print('Numer {}, in binary is {}.'.format(n, bin(b)))
elif b == 2:
    print('Number {} in octal is {}.'.format(n, oct(b)))
elif b == 3:
    print('number {} in hexadecimal is {}.'.format(n, hex(b)))

