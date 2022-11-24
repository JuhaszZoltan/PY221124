mondat:str = input('írj be egy mondatot: ')
if mondat[-1] == '?':
    print('ez egy kérdő mondat')
elif mondat[-1] == '!':
    print('ez egy felszólító, felkiáltó vagy óhajtó mondat')
elif mondat[-1] == '.':
    print('ez egy kijelentő mondat')
else: print('nem dönthető el a mondat típusa')