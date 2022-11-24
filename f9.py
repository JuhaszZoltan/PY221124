kisbetuk:str  = "abcdefghijklmnopqrstuvwxyz"
nagybetuk:str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

szoveg:str = "EbBeN vAn MiNdEnFeLe BeTu"

for k in szoveg:
    i = 0
    while i < len(kisbetuk) and kisbetuk[i] != k: i += 1
    if i < len(kisbetuk):
        ki = 0
        while k != kisbetuk[ki]: ki += 1
        print(nagybetuk[ki], end='')
    else: print(k, end='')
print()
for k in szoveg:
    if k in kisbetuk:
        print(nagybetuk[kisbetuk.index(k)], end='')
    else: print(k, end='')
print()
print(szoveg.upper())