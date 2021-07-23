"""inserir 5 numeros em uma lista, mostrar o maior valor, o menor valor e a posição de cada um"""
numeros = []
for c in range(0,5):
    numeros.append(int(input(f'Digite um número para a posição {c}: ')))
print(f'O maior número é {max(numeros)} na posição {numeros.index(max(numeros))}, o menor número é {min(numeros)} na posição {numeros.index(min(numeros))}.')