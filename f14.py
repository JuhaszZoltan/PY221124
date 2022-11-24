eb:str = 'áéíóöőúüű'
enb:str = 'aeiooouuu'

szoveg:str = 'árvíztűrő tükörfúrógép'
kopasz:str = ''

for k in szoveg:
    if k in eb:
        kopasz += enb[eb.index(k)]
    else: kopasz += k
print(f'ékezet nélkül: {kopasz}')