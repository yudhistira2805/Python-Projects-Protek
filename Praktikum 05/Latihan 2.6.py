from random import randint
print("Hai... nama saya Mr.X, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan ya!!!")
bil = randint(0, 100)
skor = 100
while(True):
    if(skor < 1):
        print("Anda sudah kalah T_T")
        break
    tebak = int(input("Tebakan Anda : "))
    if(tebak > bil):
        print("Bilangan tebakan anda terlalu besar")
    elif(tebak < bil):
        print("Bilangan tebakan anda terlalu kecil")
    else:
        print("Yeeeee...... anda BENAR :D")
        print("Skor anda : ", skor)
        break
    skor -= 2
