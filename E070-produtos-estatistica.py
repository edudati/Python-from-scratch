"""insira produtos com nome e preço. pergunte se vai continuar no final de cada produto. no final mostre:
1- total gasto na compra
2 - quantos produtos custaram mais de R$1000,00
3 - qual o nome do produto mais barato"""

soma = 0
vBarato = 99999999999999
nBarato = ''
countCaro = 0
while True:
    produto = str(input('Insira o nome do produto: '))
    valor = float(input('Insira o valor do produto: '))
    soma += valor
    if valor > 1000:
        countCaro += 1
    if valor < vBarato:
        vBarato = valor
        nBarato = produto
    continuar = str(input('Digite [S] para SAIR ou qualquer tecla para continuar: ').strip().upper())
    if continuar == 'S':
        break
print('O total gasto foi R${:.2f}\n{} produtos custaram mais de R$1000,00.\nO produto mais barato foi {}'.format(soma, countCaro, nBarato))

