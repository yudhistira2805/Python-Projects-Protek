from random import randint
print("Hai... nama saya Mr.X, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan ya!!!")
bil = randint(0, 100)
while(True):
    tebak = int(input("Tebakan Anda : "))
    if(tebak > bil):
        print("Bilangan tebakan anda terlalu besar")
    elif(tebak < bil):
        print("Bilangan tebakan anda terlalu kecil")
    else:
        print("Yeeeee...... anda BENAR :D")
        break
