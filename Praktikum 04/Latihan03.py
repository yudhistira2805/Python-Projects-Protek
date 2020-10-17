# Bensin yang Diperlukan Pak Budi

print('Menghitung Bensin Yang Diperlukan')
JarakTotal = 795
#Perbandingan Bensin per Liter dengan Jarak Tempuh
KonsumsiBensin = 1/12
TotalBensin = JarakTotal*KonsumsiBensin
print('Bensin yang diperlukan untuk perjalanan yaitu', TotalBensin, 'liter')

#Kapasitas Tanky
Tanky = 50
Kapasitas = int(TotalBensin//Tanky)
print('Pak budi perlu mengisi bensin sebanyak', Kapasitas, 'kali dalam perjalanannya')
