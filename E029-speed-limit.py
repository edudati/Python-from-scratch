""" If car is above 80k, apply traffic ticket of $7 each km above speed limit"""

vel = float(input('Car speed: '))

if vel > 80:
    velAbove = vel-80
    ticket = velAbove*7
    print('You are {:.0f}km/h above the spped limit and was fined in ${:.2f}.'.format(velAbove, ticket))
else:
    print('All right!')