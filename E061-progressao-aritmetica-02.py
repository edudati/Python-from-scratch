n = int(input('primeiro numero: '))
u = int(input('ultimo numero: '))
r = int(input('razão: '))

for c in range(n, u+r, r):
    print(c,'. ', end='')

while n < u:
    print('{} . '.format(n), end='')
    n += r
print('{}'.format(n), end='')
