#Membuka dan Akan Membaca File data.txt
try:
    file = open("D:\data.txt", "r")

#Baca Baris Pertama dari File
#Simpan ke Dalam Variabel bil1 sebagai Integer
    bil1 = int(file.readline())

#Baca Baris Pertama dari File
#Simpan ke Dalam Variabel bil2 sebagai Integer
    bil2 = int(file.readline())

#Hitung dan Tampilkan Hasil Bagi
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' = ', hasil)

except FileNotFoundError:
    print("File tidak ditemukan")
except ZeroDivisionError:
    print("Tidak boleh ada pembagian nol")
