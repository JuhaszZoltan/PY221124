from random import randrange

karakterek:str = 'abcdefgh123456789_'
pwd:str = ''

for n in range(8):
    pwd += karakterek[randrange(0, len(karakterek))]
print(f'generált jelszó: {pwd}')
