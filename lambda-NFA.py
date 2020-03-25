f = open("date.in")
cuvant=input()
nr_stari = int(f.readline())
alfabet = [x for x in f.readline().split()]
stare_initiala = int(f.readline())
stari_finale= {int(x) for x in f.readline().split()}
st=[{} for i in range(nr_stari)]
stare = f.readline()#citesc prima tranzitie


while stare!="":
    (x,y,z)=[i for i in stare.split()]#x devine prima stare din tranzitie y, devine caracterul si z devine starea in care ajungem dupa ce citim caracterul b
    if y not in st[int(x)]:
        st[int(x)][y]=set()
    st[int(x)][y].add(int(z))
    stare=f.readline()#citesc urmatoarele tranzitii

def verificare(word,stari):
    stari_noi = stari
    stari_vechi = set()
    while stari_vechi!=stari_noi:
        stari_vechi=stari_noi
        for i in stari_vechi:
            if '#' in st[i]:
                stari_noi = stari_noi.union(st[i]['#'])


    if word=="":
        return stari_finale.intersection(stari_noi)!=set()
    else:
        auxil = set()
        for i in stari_noi:
            if word[0] in st[i]:
                auxil=auxil.union(st[i][word[0]])
        return verificare(word[1:],auxil)

x= set()
x.add(stare_initiala)

print(verificare(cuvant,x))