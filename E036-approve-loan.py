""" Aprove loan to by a house:
1- Ask price os the house, salary and how many years for pay
2- The parcel cannot overcome 30% of salary
"""

house = float(input('Valor da casa: '))
salary = float(input('Salário: '))
years = float(input('Anos para pagar: '))

parcMax = salary * 0.3
nParc = years * 12
vParc = house / nParc

if vParc > parcMax:
    print('Denied')

else:
    print('Approved.\nYour parcel will be ${:.2f} per {:.0f} months.'.format(vParc, nParc))