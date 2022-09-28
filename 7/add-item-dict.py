mahasiswa = {'nama': 'Oki', 'asal': 'Indonesia', 'hobi': 'Memancing'}

#print(mahasiswa.get('hobi'))

print('Hobi dari {} adalah {}'.format(
    mahasiswa.get('nama'),
    mahasiswa.get('hobi')
))