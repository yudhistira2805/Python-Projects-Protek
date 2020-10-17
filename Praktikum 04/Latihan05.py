# Grafik Perhitungan Jumlah Mahasiswa Mahasiswa

# Input Jumlah Mahasiswa
mhsL = input("Jumlah Mahasiswa Laki-Laki : ")
mhsP = input("Jumlah Mahasiswa Perempuan : ")

# Kalkulasi
diagramL = int(mhsL) // 5
diagramP = int(mhsP) // 5

# Hasil Output Diagram
print("Laki-Laki :", '■' * int(diagramL))
print("Perempuan :", '■' * int(diagramP))
