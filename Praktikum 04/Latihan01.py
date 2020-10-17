# Program penghitung tarif sewa mobil

import math
print("Program Penghitung Tarif Sewa")
TarifSewaPertama = 200000
print("Tarif sewa 12 jam pertama",TarifSewaPertama)
TarifSewaSelanjutnya = 10000
print("Tarif sewa 1 jam selanjutnya",TarifSewaSelanjutnya)

JamMulai = 6
JamSelesai = 23
MenitMulai = 0
MenitSelesai = 50
WaktuSewa = (JamSelesai - JamMulai) + math.floor((MenitSelesai - MenitMulai) / 60)

WaktuSewaPertama = 12
WaktuSewaTambahan = WaktuSewa - WaktuSewaPertama

BiayaTambahan = WaktuSewaTambahan*TarifSewaSelanjutnya
TotalBiaya = TarifSewaPertama + BiayaTambahan

print("Tarif sewa pertama: ",TarifSewaPertama)
print("Tarif sewa tambahan: ",BiayaTambahan)
print("Total yang harus dibayar: ",TotalBiaya)
