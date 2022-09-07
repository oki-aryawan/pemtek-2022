tahun = int(input('Masukkan berapa tahun anda menabung (dalam tahun): '))
saldo = int(input('Masukkan saldo anda: '))

bunga = saldo * 0.15 # menghitung bunga dengan saldo x 15%
saldo_akhir = saldo + bunga

print(f'Saldo Awal: Rp {saldo}') # tampilkan saldo awal
print(f'Bunga: Rp {bunga}') # tampilkan bunga
print(f'Saldo Akhir: Rp {saldo_akhir}') # tampilkan saldo akhir