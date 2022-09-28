pesan = {
    'isi' : 'ONLY ONCE'
}

#isi_pesan = pesan.pop('isi')

print(f'Isi pesan: {pesan.get("isi")}')

#print(f'isi pesan: {isi_pesan}')

print('isi' not in pesan)

print(len(pesan))