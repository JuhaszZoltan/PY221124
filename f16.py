szoveg:str = '''
Semmi ágán ül szivem,
kis teste hangtalan vacog,
köréje gyűlnek szeliden,
s nézik, nézik a csillagok.'''

karakter_lista = list(szoveg.lower())
karakter_lista.sort()
rendezett_szoveg:str = ''.join(karakter_lista).strip().replace(',', '').replace('.', '')

print(rendezett_szoveg)