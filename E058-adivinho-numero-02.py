"""jugo para adivinhar um numero de 1 a 5, tendo quantas vezes necessárias para adivinhar e guardando o numero de vezes que tentou"""
import random
import time

n = int(input('Adivinhe um numero de 1 a 5: '))
escolha = random.randint(1,5)
tentativa = 1
while n != escolha:
    n = int(input('Não foi dessa vez, tente novamente: '))
    tentativa += 1
print('Parabéns, você acertou!\nPrecisou de {} palpite(s)'.format(tentativa))