a = int(input('Uang yang harus dibayar: '))
b = int(input('Jumlah yg dibayarkan: '))

def kembalian(a, b):
    kembali = b-a
    uang = {}
    if kembali > 0:
        limapuluh = kembali // 50
        uang['50-Ribu'] = limapuluh
        kembali -= 50 * limapuluh

        duapuluh = kembali // 20
        uang['20-Ribu'] = duapuluh
        kembali -=20 * duapuluh

        sepuluh = kembali // 10
        uang['10-Ribu'] = sepuluh
        kembali -= 10 * sepuluh

        lima = kembali // 5
        uang['5-Ribu'] = lima
        kembali -= 5 * lima

        dua = kembali // 2
        uang['2-Ribu'] = dua
        kembali -= 2 * dua
    if uang:
        for key, value in uang.items():
            if value>0:
                print(f'{key}: {value}')
    else:
        print('Uang pas')


print(kembalian(a,b))