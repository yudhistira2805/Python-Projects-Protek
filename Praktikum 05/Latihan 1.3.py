indo = int(input('Nilai B.Indonesia : '))
ipa  = int(input('Nilai IPA         : '))
mtk  = int(input('Nilai Matematika  : '))

if(indo >=0) and (ipa >=0) and (mtk >=0) and (indo<=100) and (ipa<=100) and (mtk <=100):
        if(indo >= 60) and (ipa >= 60) and (mtk >70):
            print("LULUS")
        else:
            sebab = ""
            if(indo<60):
                sebab += "- Nilai B.Indonesia kurang dari 60\n"
            if(ipa<60):
                sebab += "- Nilai IPA kurang dari 60\n"
            if(mtk<=70):
                sebab += "- Nilai Matematika kurang dari sama dengan 70\n"
            print("\nTIDAK LULUS")
            print("Sebab : ")
            print(sebab)
else:
    print("Maaf input tidak valid")
