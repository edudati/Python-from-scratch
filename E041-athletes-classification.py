from datetime import date

year = int(input('Year of birth: '))
age = date.today().year - year

if age <= 9:
    print('MIRIM - {} years.'.format(age))
elif 9 < age <= 14:
    print('INFANTIL - {} years.'.format(age))
elif 14 < age <= 19:
    print('JUNIOR - {} years.'.format(age))
elif 19 < age <= 25:
    print('SENIOR - {} years.'.format(age))
else:
    print('MASTER - {} years.'.format(age))
