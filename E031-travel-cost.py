""" Ask for distance of a travel in km and
returne ticket price. Consider:
1- $0,50 each km run for travels up to 200km (including 200km)
2- $0,45 for travels over 200km."""

dist = float(input('Travel distance: '))
if dist > 200:
    price = dist * 0.45
else:
    price = dist * 0.50
print('Ticket: ${:.2f}'.format(price))