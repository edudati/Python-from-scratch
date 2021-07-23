from math import factorial

n = int(input('Digite um número: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(n, f))
