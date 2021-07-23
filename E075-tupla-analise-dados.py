""""ler 4 valores e guarde numa tupla, depois mostre:
1 - quantas vezes o 9 apareceu
2- em que posição foi digitado o primeiro numero 3
quais foram os números pares"""

n = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')),
     int(input('Digite um número: ')))
print('Você digitou: {}'.format(n))
print('O número 9 apareceu {} vezes'. format(n.count(9)))
print('O primeiro 3 digitado apareceu na {}a posição.'.format(n.index(3)+1))


