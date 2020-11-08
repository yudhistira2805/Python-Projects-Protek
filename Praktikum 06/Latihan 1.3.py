#Factorial

def faktorial(n):
    hasil = n
    while(n > 1):
        n -= 1
        hasil *= n
    return hasil

def C(n, r):
    return faktorial(n) / (faktorial(n - r) * faktorial(r))

def P(n, r):
    return faktorial(n) / (faktorial(n - r))

print(P(5, 3))
print(C(10, 7))
