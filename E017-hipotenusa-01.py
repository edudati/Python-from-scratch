# Read lenght of opposite side and adjacent side of a right-angled triangle and return hypotenuse

from math import sqrt
opposite = float(input('Lenght of opposite side:'))
adjacent = float(input('Legth of adjacent side: '))
hyp = sqrt((opposite * opposite) + (adjacent * adjacent))
print("The hypotenuse is {:.2f}".format(hyp))