""" IMC calculator
Weight (kg) / Height (meter) squared"""

w = float(input('Weight kg: '))
h = float(input('Height meter: '))
imc = w / (h * h)

if imc < 18.5:
    print('IMC = {:.1f} - UNDER WEIGHT'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC = {:.1f} - IDEAL WEIGHT'.format(imc))
elif 25 <= imc < 30:
    print('IMC = {:.1f} - OVERWEIGHT'.format(imc))
elif 30 <= imc < 40:
    print('IMC = {:.1f} - OBESITY'.format(imc))
else:
    print('IMC = {:.1f} - MORBID OBESITY'.format(imc))

