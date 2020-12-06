#Fungsi
def avgBuah(n):
    sumBuah = sum(n.values())
    count = len(n.values())
    return sumBuah/count

buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Manga' : 7800, 'Duku' : 6500}
result = avgBuah(buah)
print('Rata - rata harga buah diatas adalah : ', result)
