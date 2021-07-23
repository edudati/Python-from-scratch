n = int(input('Digite um numero de termos que quer ver: '))
s1 = 0
s2 = 1
cont = 2
if n == 1:
    print('0')
elif n == 2:
    print('0 - 1')
else:
    while cont < n:
        s3 = s1+s2
        s1 = s2
        s2 = s3
        cont += 1
        print('0 - 1 - {} - '.format(s3), end='')


