
m = int(input('Masaa benda (kg): '))
g = 10 # m/s^2
p = int(input('Tekanan udara (kPa): '))
A = float(input('Luas penampang silinder (m^2): '))


def hitung_gaya(massa, gravitasi, tekanan, luas):
    F = (massa * gravitasi) + (tekanan * luas)
    print(f"Gaya: {F} Newton")


hitung_gaya(m,g,p,A)
