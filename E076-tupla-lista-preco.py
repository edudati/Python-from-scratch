"""crie uma lista de preço  numa tupla e exiba em uma tabela"""

listagem = ('Borracha', 1.50, 'lapis', 1.00, 'caderno', 7.50, 'estojo', 4.30, 'caneta', 3.05)

print('=' * 30)
print('LISTA DE PREÇOS')
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'{listagem[item]:>5}')