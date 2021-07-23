"""Ask the amount of km traveled and the number of days used and tham,
calculate the price of rental
The car is $50,00 a day plus $0.60 per km """

day = int(input('How may days of car rental? '))
km = int(input('How many km traveled? '))
price = (day * 50) + (km * 0.60)

print('The total price for the car rental is: ${:.2f}'.format(price))

