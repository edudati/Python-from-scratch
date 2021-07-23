"""digitar sexo de uma pessoa aceitando somente: [M/F]"""

sexo = str(input('Digite o sexo: [M/F] ')).strip().lower()
while sexo not in 'mf':
    sexo = str(input('Dados inválidos, por favor, digite novamente o sexo: [M/F] ')).strip().lower()
print('Obrigado, você escolheu: {}'.format(sexo.upper()))