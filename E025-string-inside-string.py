""" Search the surname 'Silva' inside a name
string inside another string"""

n = str(input('Type your full name: ')).strip()
print("Your name have 'Silva'? {}".format('silva' in n.lower()))