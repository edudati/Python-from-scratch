"""Tupla com os 15 primeiros do brasileirão
1 - mostrar 5 primeiros
2 - mostrar os 4 ultimos
3 - times em ordem alfabética
4 - Posição do time do Botafogo"""

time = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Corinthians', 'Internacional', 'Grêmio', 'Bahia', 'Atlético-PR', 'Goiás', 'Vasco', 'Atlético Mineiro', 'Botafogo', 'Fortaleza', 'Ceará')
print('Os cinco primeiros são: {}'.format(time[0:5]))
print('Os 4 ultimos são: {}'.format(time[-4:]))
print('Os times em ordem alfabética são: {}'.format(sorted(time)))
print('A posição do Botafogo é {}'.format(time.index('Botafogo')))

