n = int(input('Number: '))
total = 0

for c in range(1, n+1):
    if n % c == 0:
        total += 1
if total <= 2:
    print(n, 'It is a prime number')
else:
    print(n, 'It is NOT a prime number')