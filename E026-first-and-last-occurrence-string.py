""" How many times the letter A appears in a phrase and
return the position of the first and the last A"""

p = str(input('Type a phrase: ')).strip().lower()
print('The phrase have {} letters A.'.format(p.count('a')))
print('The first A is in {} position.'.format(p.find('a') + 1))
print('The last A is in {} position.'.format(p.rfind('a') + 1))



