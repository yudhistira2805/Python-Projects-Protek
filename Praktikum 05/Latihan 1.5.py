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
    status = int(input("Masukkan Status (1:Menikah, 2:Belum) : "))
    if(status == 1):
        tnikah = gajiP * 10/100
        anak = int(input("Masukkan Jumlah Anak : "))
        tanak = gajiP * 5/100 * anak
    elif(status == 2):
        tnikah = 0
        tanak = 0
    else:
        print("Input yang ada tidak valid")
        status = False

if(gol != False):
    print("\n================================")
    print("STRUCK RINCIAN GAJI KARYAWAN")
    print("--------------------------------")
    print("Nama Karyawan     : ",nama, " ( Kode:",kode,")")
    print("Golongan          : ",gol)

    if(status ==1):
        print("Status        : Menikah")
        print("Jumlah Anak   : ", anak)
    else:
        print("Status        : Belum Menikah")
        
    print("--------------------------------")
    print("gajiP             : ", gajiP)
    print("Tunjangan Istri   : ", tnikah)
    print("Tunjangan Anak    : ", tanak)
    print("-------------------------------- +")
    gajiK = gajiP + tnikah + tanak
    print("Gaji Kotor        : ", gajiK)
    potgaji = int(gajiK*potongan/100)
    print("Potongan (",potongan," %): ",potgaji)
    print("--------------------------------")
    gajiB = gajiK - potgaji
    print("Gaji Bersih       : ", gajiB)
