"""jogar par ou impar com o computador. o jogo será interrompido quando o jogador perder, mostrar o total de vitórias consecutivas no final"""

from random import randint
vitoria = 0
while True:
    jogador = int(input('Escolha um número de 0 a 10: '))
    escolha = str(input('Digite [P] PAR ou [I] IMPAR: ').strip().upper())
    while escolha not in 'PI':
        escolha = str(input('Escolha inválida. Digite [P] PAR ou [I] IMPAR: ').strip().upper())
    computador = randint(0,10)
    soma = jogador + computador
    if soma % 2 == 0:
        if escolha == 'P':
            print('Você venceu!')
            vitoria += 1
        else:
            if vitoria == 0:
                print('Você perdeu.')
            elif vitoria == 1:
                print(f'Você perdeu.\nVocê conquistou 1 vitória.')
            else:
                print(f'Você perdeu.\nVocê conquistou {vitoria} vitórias seguidas.')
            break
    if soma % 2 == 1:
        if escolha == 'I':
            print('Você venceu!')
            vitoria += 1
        else:
            if vitoria == 0:
                print('Você perdeu.')
            elif vitoria == 1:
                print(f'Você perdeu.\nVocê conquistou 1 vitória.')
            else:
                print(f'Você perdeu.\nVocê conquistou {vitoria} vitórias seguidas.')
            break


