"""Read name, age, gender of 5 peoples
Average of ages
Name of older man
How many women has less than 20 years old"""

avgAge = 0
olderAge = 0
olderName = ''
countWoman = 0
for p in range(1,6):
    name = str(input('Name: '))
    age = int(input('Age: '))
    gender = str(input('Gender: ')).lower()
    avgAge += age
    if gender == 'm' and olderAge < age:
        olderAge = age
        olderName = name
    if gender == 'f' and age < 20:
        countWoman += 1
avgAge = avgAge / 5
print('Average of age is {} years.'.format(avgAge))
print('Name of older man {}.'.format(olderName))
print('There are {} women with less than 20 years old.'.format(countWoman))