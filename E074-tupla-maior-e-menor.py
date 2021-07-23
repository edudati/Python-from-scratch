"""gerar 5 números aleatórios em uma tupla, exibir a lista, exibir o maior número e o menor número"""
from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(n)
print(max(n))
print(min(n))