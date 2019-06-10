def wczytaj(nazwa):
    with open(nazwa) as plik:
        return list(map(str.strip, plik))
liczby=wczytaj('liczby.txt')
q=0
p2=0
p8=0
max=0
mini=10000
gmax=0
gmini=0
v=1
for x in liczby:
    p=(''.join(sorted(x)))
    if p[len(p)//2]=='0':
        q+=1;
    if x[-1]=='0':
        p2+=1
    if x[-3:]=='000':
        p8+=1
    if int(x)>max:
        max=int(x)
        gmax=v
    if int(x)<mini:
        mini=int(x)
        gmini=v
    v+=1
wyjscie = open("wyjscie.txt", "w")
wyjscie.write('4.1:\n'+str(q))
wyjscie.write('\n4.2:\n'+str(p2)+'\n'+str(p8))
wyjscie.write('\n4.3:\n'+str(gmini)+'\n'+str(gmax))
