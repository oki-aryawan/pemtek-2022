class Mahasiswa:
    """

    Kelas ini digunakan untuk mendefinisikan objek Mahasiswa di kehidupan nyata

    """


    def __init__(self, nama, asal):
        self.asal = asal
        self.nama = nama

    def perkenalan(self):
        print(f'Perkenalkan saya {self.nama} dari {self.asal}')


Budi = Mahasiswa('Budi', 'Sulawesi')
Wati = Mahasiswa(asal='Sumatera', nama='Susilowati')


Budi.perkenalan()
Wati.perkenalan()
print(Mahasiswa.__doc__)