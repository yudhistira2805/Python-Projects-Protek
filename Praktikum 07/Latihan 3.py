print("-------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("-------------------------")

lagi = 'Yes'
total = 0
n = 0

while True:
    try:
        bil = int(input("Masukkan nilai bilangan bulat            : "))
        
    except ValueError:
        print("Angka yang anda masukkan bukan bilangan bulat")
        continue

    total += bil
    n += 1
    lagi = input("Lagi? (Yes/No)                           : ")
    if (lagi == "Yes"):
        continue
    else:
         break

hasil = total/n
print("\nRata-rata data yang anda masukkan adalah : ", hasil)
