"""Read the width and height of the wall and and calculate how much paint is needed to paint the wall,
knowing that every liter of paint paints 2 square meters. """

width = float(input('Type the width of the wall: '))
height = float(input('Type the height of the wall: '))
area = width * height
liter = area / 2

print('The area to be painted is {:.1} square meters. You will need {:.1} liter(s) of paint.'.format(area, liter))

