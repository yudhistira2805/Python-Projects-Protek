dir = input("Masukkan direktori & nama file : ")
lagi = 'Yes'

try:
    file = open(dir, "r")
    while True:
        file = open(dir, 'a')
        a = input("Data yang mau ditambahkan : ")
        file.write(a)
        lagi = input("Mau tambah lagi? (Yes/No) : ")
        if (lagi == 'Yes'):
            continue
        else:
            print("Data berhasil ditambahkan")
            break

    file.close()
except FileNotFoundError:
    print("Maaf file tidak ditemukan")
