
n1 = float(input('value 1: '))
n2 = float(input('value 2: '))
average = (n1 + n2) / 2
if average < 5:
    print('Average:  {:.2f}, Reproved.'.format(average))
elif 4.9 < average < 7:
    print('Average {:.2f}, Recovery.'.format(average))
else:
    print('Average: {:.2f}, Approved.'.format(average))
