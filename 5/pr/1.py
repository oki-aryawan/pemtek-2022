angka = int(input("Masukkan angka positif: "))
nilai_akhir = 0

if angka > 0:
    for i in range(1, angka+1):
        nilai = (2 * i) - 1
        nilai_akhir += nilai
    print(f"Hasil {angka}^2 adalah {nilai_akhir}")
else:
    print('Maaf, perhitungan tidak dapat dilakukan')