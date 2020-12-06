#Perhitungan Kuadrat
def kuadrat(bil):
    for i in range(len(bil)):
        bil[i] **= 2
    return bil

#Nilai Bilangan
print(kuadrat([4,8,1,43]))
