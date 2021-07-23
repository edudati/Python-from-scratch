"""inserir numeros numa lista e se o numero existir, o numero nao é adicionado. exibir a lista de numeros em ordem crescente e descrescente"""

numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n in numeros:
        print('Esse número já existe!')
    else:
        numeros.append(n)
    continua = str(input('Digite [S] para Sair ou qualquer tecla para continuar: ')).strip()
    if continua in 'Ss':
        break
print('Crescente')
print(sorted(numeros))
print('Decrescente')
print(sorted(numeros, reverse=True))
