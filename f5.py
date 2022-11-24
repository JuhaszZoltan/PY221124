#       0  1  2  3
#INPUT: B  É  K  A

szo:str = input('írj be egy szót: ')
for i in range(len(szo)):
    print(szo[len(szo) - 1 - i], end='')
print()

betuk:list[chr] = []
for k in szo: betuk.append(k)
list.reverse(betuk)
for b in betuk: print(b, end='')