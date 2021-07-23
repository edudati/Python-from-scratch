"""ler varios numeros e colocar em uma lista,
1 - quantos numeros foram digitados
2 - a lista de valores ordenada de forma descrescente
3 - se o número 5 foi digitado"""

numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    continua = str(input(('digite [S] para sair ou qualquer tecla para continuar: ')))
    if continua in 'Ss':
        break
print(f'Foram digitados {len(numeros)} numeros.')
print(f'Os numeros digitados foram {sorted(numeros, reverse=True)}')
print(f'Existe o número 5 na lista: {5 in numeros}')