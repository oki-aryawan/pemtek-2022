bobot = [] # ini list kosong

n = int(input('Masukkan jumlah bobot yang anda ingginkan: ')) # ni jumlah bobot
for i in range (0, n):
    nilai = int(input(f'Masukkan bobot ke-{i+1}: ')) # input nilai bobotnya
    bobot.append(nilai) # ni masukin nilai bobot yg diinput oleh user

print('Nilai bobot awal: ', bobot)
print('Nilai bobot diurutkan: ',sorted(bobot)) # ni pakai metode sorted
print('Nilai rata-rata bobot: ', sum(bobot)/len(bobot)) # ni rata-rata