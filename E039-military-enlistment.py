""" Read the year of birth and return if he need to enlist, is is not time to enlist, or if the time to enlist is over
In case of lake of time or delay, show the time"""


from datetime import date
year = int(input('Year of birth: '))
age = date.today().year - year
if age < 18:
    print('It is not time to enlist. See you in {} year(s).'.format(18 - age))
elif age > 18:
    print('The time to enlist is over. You are {} year(s) late.'.format(age - 18))
else:
    print('It is time to enlist, look for the nearest location.')