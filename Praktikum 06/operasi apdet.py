from operation import *

print(' 2 + 4 * 6 - 4                =  ', kurang(tambah(2, kali(4, 6)), 4))
print('(4 + 7) * (6 - 9)             = ', kali(tambah(4, 7), kurang(6, 9)))
print('(10 + 2) / (7 + 5) / (12 -34) =  ', bagi(bagi(tambah(10, 2), tambah(7, 5)), kurang(12, 34)))
