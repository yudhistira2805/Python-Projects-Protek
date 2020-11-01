kode = input("Masukkan Kode Karyawan : ")
nama = input("Masukkan Nama Karyawan : ")
gol  = input("Masukkan Golongan      : ")

if(gol == "A"):
    gajiP = 10000000
    potongan = 2.5

elif(gol == "B"):
    gajiP = 8500000
    potongan = 2.0

elif(gol == "C"):
    gajiP = 700000
    potongan = 1.5

elif(gol == "D"):
    gajiP = 7000000
    potongan = 1.5
else:
    golongan = False
    print("Tidak Masuk Golongan")

if(gol != False):
    print("\n================================")
    print("STRUCK RINCIAN GAJI KARYAWAN")
    print("--------------------------------")
    print("Nama Karyawan     : ",nama, " ( Kode:",kode,")")
    print("Golongan          : ",gol)
    potgaji = int(gajiP*potongan/100)
    gajiber = gajiP - potgaji
    print("Gaji Pokok        : ",gajiP)
    print("Potongan (",potongan," %): ",potgaji)
    print("--------------------------------")
    print("Gaji Bersih       : ", gajiber)
