# randomly draw a student

import random

n1 = str(input('1 Student: '))
n2 = str(input('2 Student: '))
n3 = str(input('3 Student: '))
n4 = str(input('4 Student: '))
students = [n1, n2, n3, n4]
draw = random.choice(students)
print('The student selected was: {}'.format(draw))