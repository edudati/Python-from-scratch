""" Read int numbers and sum only evens"""

sEven = 0
sOdd = 0
cont = 0
sTotal = 0
for c in range(1,7):
    num = int(input('Type value {}:'.format(c)))
    if num % 2 == 0:
        sEven += num
    else:
        sOdd += num
    sTotal += num
    cont += 1
print('There are {} values.\nSum total = {}\nSum of even = {}\nSum of odds = {}'.format(cont, sTotal, sEven, sOdd))
