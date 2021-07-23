""" digitar varios numeros em uma lista, mostrar a lista e mostrar outras duas listas divididas entre pares e impares"""

todos = []
pares = []
impares = []

while True:
    todos.append(int(input('Digite um numero: ')))
    continua = str(input(('digite [S] para sair ou qualquer tecla para continuar: ')))
    if continua in 'Ss':
        break
for i, v in enumerate(todos):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=-=-=-=-=-=- Lista com TODOS -=-=-=-=-=-=-=-')
print(todos)
print('\n')
print('-=-=-=-=-=-=- Lista com IMPARES -=-=-=-=-=-=-=-')
print(impares)
print('\n')
print('-=-=-=-=-=-=- Lista com PARES -=-=-=-=-=-=-=-')
print(pares)
