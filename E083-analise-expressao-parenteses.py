"""digitar uma expressão que utilize parenteses, e analisar se a expressão passada está com os parenteses abertos ou fechados na ordem correta"""
e = str(input('Digite a expressão: '))
lista = []

for c in e:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Certo')
else:
    print('Errado')
