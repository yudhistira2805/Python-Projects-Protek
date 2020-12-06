#Fungsi
def buahMahal(n):
    hbuah = list(n.values())
    nbuah = list(n.keys())
    hmaks = max(hbuah)
    inharga = hbuah.index(hmaks)
    print(nbuah[inharga])

#List Harga
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Manga' : 7800, 'Duku' : 6500}
buahMahal(buah)
