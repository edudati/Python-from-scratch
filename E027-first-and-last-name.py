"""Type a name and return the first and the last name"""

n = str(input('Type your full name: ')).strip()
nList = n.split()
print('First name: {}'.format(nList[0]))
print("Last name: {}".format(nList[len(nList)-1]))
