nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50,  'uas' : 80}, 
 	 {'nim' : 'A02', 'nama' : 'Budi',     'mid' : 40,  'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha',   'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna',    'mid' : 20,  'uas' : 100}, 
	 {'nim' : 'A05', 'nama' : 'Fatimah',  'mid' : 70,  'uas' : 100}]

print('='*75)
print('NIM'.ljust(10), 'NAMA'.ljust(15), 'N.MID'.rjust(5), 'N.UAS'.rjust(10), 'N.AKHIR'.rjust(10), 'STATUS'.rjust(10))
print('-'*75)
for daftar in nilai:
    nAkhir = int((daftar['mid']+2*daftar['uas'])/3)
    if nAkhir >= 60:
        status = 'Lulus'
    else:
        continue
    print(daftar['nim'].ljust(10), daftar['nama'].ljust(15), str(daftar['mid']).rjust(5), str(daftar['uas']).rjust(10), str(nAkhir).rjust(10), status.rjust(10))
print('-'*75)
