"""
Made in 2 different ways
"""

for n in range(1, 51):
    print('.', end='')
    if n % 2 == 0:
        print(n, end='')

print('\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

for n in range(0, 51, 2):
    print('.', end='')
    print(n, end='')