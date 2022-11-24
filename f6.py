szo:str = input('írj be egy szót: ')
esz:int = 0
for k in szo:
    if k in 'Ee': esz += 1
print(f'"e" betűk száma: {esz}')