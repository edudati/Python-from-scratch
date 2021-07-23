"""ler vários numeros inteiros no teclado, mostrar quantos numeros foram digitados e a soma entre eles. a condição de parada é digitar o 999, sendo que a flag não entra na conta."""

n = int(input('Digine um número ou 999 para sair: '))
count = 0
total = 0
while n != 999:
    count += 1
    total += n
    n = int(input('Digite outro número ou 999 para encerrar: '))
print('A soma é {} e o total de números inseridos é {}'.format(total, count))