from random import randint
hitung = 1
while True:
    bil = randint(0, 10)
    print(bil)
    if bil == 5:
        print("Jumlah Perulangan : ", hitung)
        break
    hitung += 1
