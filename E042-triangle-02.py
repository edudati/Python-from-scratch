""" Check if the triangle is isocceles (2 sides the same),
scalene (all different sides) or
equilateral (all same sides)"""

l1 = float(input('Side 1: '))
l2 = float(input('Side 2: '))
l3 = float(input('Side 3: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    if l1 == l2 == l3:
        print('EQUILATERAL')
    elif l1 != l2 != l3:
        print('SCALENE')
    else:
        print('ISOCELES')
else:
    print('IS NOT A TRIANGLE')