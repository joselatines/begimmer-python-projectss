dic = {
  'name': 'Name is a definition of name',
  'idk': 'a real good definition'
}

available = ''

for x in dic:
  available += str(x) + ', '
  
print(f'Words available: {available}')

answer = input('Choose a word: ')

if answer in dic:
  print(dic[answer])
else: print('That word does not exits')