"""nome e peso de varias pessoas
1-numero de pessoas cadastradas
2-lista das pessoas mais pesadas para os mais leves
3-lista das pessoas mais leves para as mais pesadas"""
lTemp = []
lista = []
lOrdenada = []
while True:
    lTemp.append(str(input('Digite o nome: ')))
    lTemp.append(float(input('Digite o peso: ')))
    lista.append(lTemp[:])
    lTemp.clear()
    '''para criar uma cópia sem depender de uma lista para outra inserir o [:]'''
    continua = str(input(('digite [S] para sair ou qualquer tecla para continuar: ')))
    if continua in 'Ss':
        break
lOrdenada.append(sorted(lista, key=lambda x: x[1]))
print(f'A lista tem {len(lOrdenada)} pessoas cadastradas.')
print('da mais magra para a mais gorda: ', end='')
for p in len(lOrdenada):
    print(p[0], end='')
print('\n\nda mais gorda para a mais magra: ', end='')
for r in range(len(lOrdenada), 0, -1):
    print(r[0], end='')


print(lista)
print()
print(lOrdenada[:3])
print(lOrdenada[-1])