a = int(input('Nilai awal: ')) # input nilai satu
b = int(input('Nilai akhir: ')) # input nilai dua


def bilanganPrima(awal, akhir):
    hasil = []
    for i in range(awal, akhir):
        for j in range(2, i):
            if i%j != 0:
                hasil.append(i)
                print(i)
    return hasil


print(bilanganPrima(a+1, b))
