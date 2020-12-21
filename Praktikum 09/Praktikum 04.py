import random
def shuffleString(x, y):
    lis = []
    x = list(x)
    n = 0
    while True:
        n += 1
        rdm = (random.sample(x,len(x)))
        gabung = ''.join(rdm)
        if (gabung in lis):
            n -= 1
        else:
            lis += [gabung]
        if (n == y):
            break
    return print(lis)

#String Yang Akan Di-Shuffle
shuffleString('saya', 4)
