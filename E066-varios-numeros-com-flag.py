"""ler vários numeros inteiros no teclado, mostrar quantos numeros foram digitados e a soma entre eles. a condição de parada é digitar o 999, sendo que a flag não entra na conta."""

count = soma = 0
while True:
    n = int(input('Digine um número ou 999 para sair: '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'A soma é {soma} e o total de números inseridos é {count}')