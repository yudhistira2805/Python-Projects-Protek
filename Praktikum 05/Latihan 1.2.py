indo = int(input('Nilai B.Indonesia : '))
ipa  = int(input('Nilai IPA         : '))
mtk  = int(input('Nilai Matematika  : '))

if(indo >=0) and (ipa >=0) and (mtk >=0) and (indo<=100) and (ipa<=100) and (mtk <=100):
        if(indo >= 60) and (ipa >= 60) and (mtk >70):
            print("LULUS")
        else:
            print("TIDAK LULUS")
else:
    print("Maaf input tidak valid")
