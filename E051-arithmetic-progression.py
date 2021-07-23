n = int(input('1st numbr: '))
u = int(input('last number: '))
r = int(input('ratio: '))

for c in range(n, u+r, r):
    print(c,'. ', end='')