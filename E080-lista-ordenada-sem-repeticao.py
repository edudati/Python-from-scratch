"""digitar cinco valores em uma lista e colocar já de forma ordenada sem utilizar o comando sort. no final mostre a lista ordenada na tela"""

lista = list()
for c in range(0,5):
    numero = int(input('Digite um número: '))
    if c == 0 or numero > lista[-1]:
        ''' lista[-1] para inserir se digitarmos um numero que seja maior que todos da lista
        o c == 0 se for o primeiro numero registrado'''
        lista.append(numero)
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                break
            posicao += 1
print(lista)