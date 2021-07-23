"""simulação de caixa eletronico, pergunte o valor sacado (numero inteiro), o programa vai falar quantas celular de cada valor serão entregues"""

print('='*30)
print('{:^30}'.format('Banco'))
print('='*30)

n = int(input('Digite o valor: '))
total = n
ced = 100
tCed = 0
while True:
    if total >= ced:
        total -= ced
        tCed += 1
    else:
        print('{} cédulas de R${:.2f}'.format(tCed, ced))
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        tCed = 0
        if total == 0:
            break

