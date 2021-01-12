from datetime import *
from dateDiff import *

myDoc = open('PerPus.txt', 'r')
read = myDoc.readlines()
Daftar = []

i = 0
for data in read:
    split = read[i].split('|')
    Daftar.append(split)
    i += 1

KMember = input('Masukkan Kode Member : ')

result = False
n = 0
for lists in Daftar:
    if KMember in Daftar[n]:
        a = 0
        for lists in Daftar:
            if KMember == Daftar[a][0]:
                date1 = datetime.date(datetime.now())
                date2 = diffDate(Daftar[a][4])
                if date2 == None or date2 < 8:
                    date2 = 0
                else:
                    date2 = date2
                print('='*35)
                print('Data Peminjaman Perpustakaan')
                print('='*35)
                print('Kode Member         : '+ Daftar[a][0])
                print('Nama Member         : '+ Daftar[a][1])
                print('Judul Buku          : '+ Daftar[a][2])
                print('Tanggal Pinjam      : '+ Daftar[a][3])
                print('Durasi Pinjam       : '+ str.rstrip(Daftar[a][4]))
                print('Tanggal Kembali     : '+ str(date1))
                print('Keterlambatan       : '+ str(date2)+ '(hari)')
                print('Penalti  /  Denda   : Rp'+str(date2*2000))
                print('-'*35)
                result = True
                break
            else:
                a += 1
    n += 1
    
if result == False:
    print('Data Invalid :(')
