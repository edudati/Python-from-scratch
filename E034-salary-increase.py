""" Saraly increase:
 1- 10% if greater than $1250
 2- 15% if smaller than $1250 inclusive"""

n = float(input('Salary: '))
if n > 1250:
    print('${:.2f}'.format(n*1.1))
else:
    print('${:.2f}'.format(n * 1.15))