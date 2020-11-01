bil = 0
hitung = 0
jml = 0
while(bil<=100):
    if(bil % 2 == 1):
        hitung += 1
        jml += bil
        print(bil)
    bil += 1
print("\nBanyaknya bilangan ganjil : ",hitung)
print("----------------------------------")
print("Jumlah seluruh bilangan   : ",jml)
