from random import shuffle

szavak = ['pulyka', 'korcsolya', 'bagoly', 'hajó', 'lyukas', 'pálya', 'folyó', 'jósnő', 'muszáj', 'fogvájó']

shuffle(szavak)

pontszam:int = 0
ssz:int = 1
for szo in szavak:
    rp:str = 'j' if 'j' in szo else 'ly'
    print(f'{ssz}.) {szo.replace(rp, "_")}', end=': ')
    ssz += 1
    betu:str = input().lower()
    if betu in ['j', 'ly'] and betu in szo:
        pontszam += 1
print(f'{len(szavak)} feladványból {pontszam} db helyes volt!')