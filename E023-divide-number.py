"""digitar um numero e mostrar os digitos separados"""

n = int(input('Type a number: '))

unit = n // 1 % 10
dozen = n // 10 % 10
hundred = n // 100 % 10
thousand = n // 1000 % 10

print('Unit: {}'.format(unit))
print('Dozen: {}'.format(dozen))
print('Hundred: {}'.format(hundred))
print('Thousand: {}'.format(thousand))





