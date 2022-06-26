alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('Gizlin danisiq cumleni kodlashdirmaq ucun crypto yazin movcud olan cumleni dekodlashdirma ucun decrypt yazin ')

text = input("cumleni yazin bitishik ara qoymayin: ").lower()
shift = int(input('reqem secin 1-26-ya '))

def encrypt(text, shift):
  ciper_text = ''
  for i in text:
    x=alphabet.index(i)
    x = x + shift
    ciper_text += alphabet[x]
  print(f'Kodlanmish cumle {ciper_text}')

def dencrypt(text, shift):
  ciper_text = ''
  for i in text:
    x=alphabet.index(i)
    x = x - shift
    ciper_text += alphabet[x]
  print(f'decok olunmus cumle {ciper_text}') 
 
if direction == 'crypto':
  encrypt(text, shift)
elif direction == 'decrypt':
  dencrypt(text, shift)