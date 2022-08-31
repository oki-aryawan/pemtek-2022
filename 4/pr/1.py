penjualan = int(input('Masukkan penjualan: '))
komisi = 0 # inisiasi komisi awal Rp 0

if penjualan <= 500000:
    komisi = 0
elif 500000 < penjualan <= 1000000:
    komisi = 0.1 * penjualan # komisi 10%
elif penjualan > 1000000:
    komisi = 50000 + ((penjualan-1000000)*0.05)

print(f'Penjualan: Rp {penjualan}')
print(f'Komisi: Rp {int(komisi)}')