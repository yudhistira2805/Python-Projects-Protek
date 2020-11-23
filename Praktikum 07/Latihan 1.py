dir = input("Masukkan direktori & nama file : ")

try:
    file = open(dir, "r")
    print("Isi file", dir,"adalah :\n",file.read())

except FileNotFoundError:
    print("File Anda Tidak Ditemukan")
