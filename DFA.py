cuvant=input()
f = open("date.in")
nr_stari = int(f.readline())
alfabet = [x for x in f.readline().split()]
stare_initiala = int(f.readline())
stari_finale = [int(x) for x in f.readline().split()]
keycaracter=[{} for i in range(nr_stari)]
stare = f.readline()


while stare!="":
    (x,y,z)=[i for i in stare.split()]
    keycaracter[int(x)][y]=int(z)
    stare=f.readline()



def verificare(S,word):
    if word=="":
        return S in stari_finale
    else:
        if word[0] in keycaracter[S]:
            S = keycaracter[S][word[0]]
            return verificare(S,word[1:])
        else:
            return False


print(verificare(0,cuvant))