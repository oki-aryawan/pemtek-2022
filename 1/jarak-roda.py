print('Program Menghitung Jarak Tempuh Roda')

jari2 = int(input('Jari-jari roda (dalam cm): '))


def hitung_jarak(jari):
    keliling = (2 * jari) * 3.14
    jarak = 2 * keliling
    print(f"Jari-jari: {jari} cm, Diameter: {2 * jari} cm")
    print(f"Keliling: {round(keliling, 2)} cm")
    print(f"Jarak tempuh: {round(jarak, 2)} cm")


hitung_jarak(jari2)

