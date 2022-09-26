def tampil (batas, i = 1):
    if i < batas:
        print(i)
        tampil(batas, i + 1)
        #print(i)
    #print(f'Perulangan ke {i}')
tampil(5)