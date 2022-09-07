#sistem penyiraman

print('Keterangan Kode umur: \n A (1-20 hari) \n B (21-40 hari) \n C (41-60 hari)')
print('Keterangan kode waktu pemberian air: \n 1(Siang) \n 2(Sore)')
umur = input('Pilih kode umur tanaman: ')
umur = umur.upper()
waktu = input('Pilih kode waktu siram: ')
air = 0
status = ''

if umur == 'A':
    status = '1-20 hari'
    if waktu == '1':
        air = 15
    elif waktu == '2':
        air = 10
elif umur == 'B':
    status = '21-40 hari'
    if waktu == '1':
        air = 40
    elif waktu == '2':
        air = 20
elif umur == 'C':
    status = '41-60 hari'
    if waktu == '1':
        air = 20
    elif waktu == '2':
        air = 5

print(f"\nKode : {status}")
print(f"Lama waktu pemberian air: {air}")






