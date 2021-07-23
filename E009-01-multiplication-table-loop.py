# Retur a multiplication table (1 to 10) using loop

x = int(input('Type a number to see your multiplication table: '))

for i in range(10):
    print('{} x {:2} = {:2}'.format(x, i+1, x*(i+1)))