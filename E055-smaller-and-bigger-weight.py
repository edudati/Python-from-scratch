smaller = 300000
bigger = 0
smallerPerson = 0
biggerPerson = 0
for c in range(1, 6):
    weight = float(input('Weight {}'.format(c)))
    if weight > bigger:
        bigger = weight
        biggerPerson = c
    if weight < smaller:
        smaller = weight
        smallerPerson = c
print('A pessoa {} teve o maior peso, {}kg.\nA pessoa {} teve o menor peso, {}kg.'.format(biggerPerson, bigger, smallerPerson, smaller))