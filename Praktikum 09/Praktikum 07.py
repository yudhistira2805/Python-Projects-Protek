mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO'         , 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR'  ]
print('='*60)
print('NIM'.ljust(5), 'N.MAHASISWA'.ljust(20), 'TGL.LAHIR'.ljust(20), 'TMPT.LAHIR'.rjust(10))
print('-'*60)
for daftar in mhs:
      data = daftar.split(':')
      nim = data[0]
      nmhs = data[1]
      tgl = data[2].split('-')
      tgl = tgl[2]+'-'+tgl[1]+'-'+tgl[0]
      tmpt = data[3]
      print(nim.ljust(5), nmhs.ljust(20), tgl.ljust(20), tmpt)
print('-'*60)
