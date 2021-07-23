"""ler varios numeros inteiros, mostrar a media, qual o maior, o menor. deve perguntar se quer continuar ou não a digitar outro numero"""


n = int(input('Digite um número: '))
continuar = True
total = 0
count = 0
maior = 0
menor = 99999999999999999999999999999
while continuar:
    total += n
    count += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    sair = str(input('Presione S para continuar ou qualquer outra letra para sair? ').strip().lower())
    if sair == 's':
        n = int(input('Digite outro número: '))
    else:
        continuar = False
media = total / count
print('A média dos números digitados foi {}.\nO maior número foi {}.\nO menor número foi {}.\n'.format(media, maior, menor))
