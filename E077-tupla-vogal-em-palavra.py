"""fazer uma tupla com varias palavras e criar um programa que extrai as vogais de cada palavra"""

palavras = ('aprender', 'programar', 'escola', 'aula', 'veiculo', 'navio', 'violao')

for p in palavras:
    print(f'A palavra {p} tem as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
    print('\n')
