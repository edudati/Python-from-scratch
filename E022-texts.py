""" insert full name and return:
1 - Name in all capital letters
2 - How many letters without spaces
3 - How many letters has the first name
"""

name = str(input('Type your full name: ')).strip()
""".strip: strip the spaces before and after"""
nDivided = name.split()
""".split: divide a string (in spaces) and create a list"""

print('YOUR NAME IN CAPITAL LETTERS: {}'.format(name.upper()))
print('Your name in small letters: {}'.format(name.lower()))
print('Your name have {} letters.'.format(len(name) - name.count(' ')))
print('Your first name have {} letters.'.format(name.find(' ')))
print('Your first name is {}, and have {} letters.'.format(nDivided[0], len(nDivided[0])))
