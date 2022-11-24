maganhangzok:str = 'aAáÁeEéÉiIíÍoOóÓöÖőŐuUúÚüÜűŰ'

szoveg:str = '''
Miért legyek én tisztességes? Kiterítenek úgyis!
Miért ne legyek tisztességes! Kiterítenek úgyis.
'''
mghsz:int = 0
for k in szoveg:
    if k in maganhangzok: mghsz += 1
print(f'magánhangzók száma a szövegben: {mghsz}')