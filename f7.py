szoveg:str = '''Kazánt súroltam; vágtam sarjat;
Elnyúltam rothadt szalmazsákon;
Bíró elítélt; hülye csúfolt;
Pincéből tódult ragyogásom.'''

c:int = 0
for k in szoveg:
    if k in ' \n': c += 1
print(f'szavak száma: {c + 1}')

# alt:
print(f'szavak száma: {len(szoveg.split())}')