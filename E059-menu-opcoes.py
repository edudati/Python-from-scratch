"""inserir 2 numeros, escolher a operação a ser feita, começar novamente ou sair do programa"""

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('\n[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - NOVOS NÚMEROS\n[5] - SAIR DO PROGRAMA')
opcao = str(input('Escolha a opção: '))
while opcao not in '12345':
    opcao = int(input('Opção inválida, escolha novamente: '))
if opcao == '1':
    r = n1+n2
    print('A soma é {}'.format(r))
elif opcao == '2':
    r = n1*n2
    print('O produto {}'.format(r))
elif opcao == '3':
    if n1 > n2:
        print('O maior é {}'.format(n1))
    elif n1 < n2:
        print('O maior é {}'.format(n2))
    else:
        print('Os númmeros são iguais.')
elif opcao == '4':
    print('Digite novamente')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    """propositalmente essa função não leva a lugar nenhum... simplesmente ele digita os 2 valores"""
else:
    print('Finalizando...')
