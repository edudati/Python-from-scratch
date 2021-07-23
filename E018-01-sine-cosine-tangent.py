# To read an angle and return sine, cosine and tangent

import math
angle = float(input('type an angle: '))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print('The angle has {:.2f} degrees, the sine is {:.2f}, the cosine is {:.2f} and the tangent is {:.2f}.'.format(angle, sine, cosine, tangent))
