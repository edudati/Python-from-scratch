""" Sale price based on payment conditions"""

price = float(input("Price: "))
print('Payment options:\n'
      '1 - Cash\n'
      '2 - Credit Card\n'
      '3 - 2x Credit Card\n'
      '4 = 3x or more Credit Card')
p = int(input("Type option: "))

if p == 1:
    price = price * 0.9
elif p == 2:
    price = price * 0.95
elif p == 4:
    price *= 1.2
print('${:.2f}'.format(price))
