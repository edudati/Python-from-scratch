phase = str(input('Phrase: ')).strip().upper()
word = phase.split()
u = ''.join(word)
contrary = ''

for letter in range(len(u) - 1, -1, -1):
    contrary += u[letter]
print(phase)
print(word)
print(u)
print(contrary)
if u == contrary:
    print('palindrome')
else:
    print('NOT palindrome')