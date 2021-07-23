""" Check if the year is bissest
1- Divisible by 4 and rest 0
2- Cannot be divisible by 100 and est different of 0
3- Maybe it can be divisible by 400 and rest 0
4 - type 0 for present year
"""

from datetime import date
year = int(input('year: '))
if year == 0:
    year = date.today().year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Bissest')
else:
    print('Not bissest')