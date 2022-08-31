# Kode Masa Tumbuh Tanaman

ms = input("Kode: ")
tetes = 0

if ms == "Bibit":
    tetes = 10
elif ms == "Pertumbuhan":
    tetes = 8
elif ms == "Pembungaan":
    tetes = 5
elif ms == "Penuaan":
    tetes = 3

print(f'Masa Tumbuh: {ms}')
print(f'Jumlah Tetes per detik: {tetes}')