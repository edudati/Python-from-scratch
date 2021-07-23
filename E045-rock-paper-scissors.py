from random import randint

print('[1] Rock\n[2] Paper\n[3] Scissor\n')
player = int(input('Choose your move: '))
comp = randint(1,3)
if (player == 1 and comp == 1) or (player == 2 and comp == 2) or (player ==3 and comp ==3):
    print('TIE')
elif (player == 1 and comp == 3) or (player == 2 and comp == 1) or (player == 3 and comp == 2):
    print('COMPUTER: {}\nYOU: {}'.format(comp, player))
    print('YOU WIN')
else:
    print('COMPUTER: {}\nYOU: {}'.format(comp, player))
    print('YOU LOOSE')