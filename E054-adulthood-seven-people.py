from datetime import date
totalSmall = 0
totalBigger = 0
for c in range(1, 8):
    year = int(input("Year of birth {}:  ".format(c)))
    age = date.today().year - year
    if age < 21:
        totalSmall +=1
    else:
        totalBigger +=1
print('We have {} people with less than 21 years old, and {} peoples older.'.format(totalSmall, totalBigger))