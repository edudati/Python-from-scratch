"""ler dados do grupo idade e sexo de várias pessoas. a cada pessoa o programa pergunta se quer continuar e non final mostra:
1 - quantas pessoas tem mais de 18 anos
2 - quantos homens foram cadastrados
3 - quantas mulheres com menos de 20 anos"""
maior = 0
homens = 0
mulheres = 0
continuar = ''
while True:
    idade = int(input('Digite a idade em anos: '))
    sexo = str(input('Digite o sexo: [F] Feminino ou [M] Masculino').strip().upper())
    while sexo not in 'FM':
        sexo = str(input('Escolha inválida. Por favor, digite novamente o sexo: [F] Feminino ou [M] Masculino').strip().upper())
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = str(input('Precione [S] para encerrar ou qualquer tecla para continuar: ').strip().upper())
    if continuar == 'S':
        break
print(f'{maior} pessoas maiores de 18 anos.\n{homens} homens cadastrados.\n{mulheres} mulher(s) com menos de 20 anos.')
