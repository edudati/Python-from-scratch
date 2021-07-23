"""mostrar tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário, o programa será interrompido quando o usuário digitar um número negativo."""

while True:
    n = int(input('Digite um número para a tabuada (ou um número negativo para sair):'))
    if n < 0:
        break
    else:
        print('\n')
        for c in range(1, 11):
            print('{:2}  x {:2} = {:2}'.format(c, n, c*n))
        print('\n-=-=-=-=-=-=-=-=-=-=-\n')
