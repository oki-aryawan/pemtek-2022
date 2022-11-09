class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        print('fungsi Orang.__init__() dieksekusi')

    def perkenalan(self):
        print(f'Perkenalkan nama saya {self.nama} dari {self.asal}')


class Pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        super().__init__(nama, asal)
        self.sekolah = sekolah


class Pekerja(Orang):
    def __init__(self, nama, asal, tempat_kerja):
        Orang.__init__(self, nama, asal)
        self.tempat_kerja = tempat_kerja



deni = Pelajar('Deni', 'Makasar', 'SMA')
deni.perkenalan()
print(f'Saya sekolah do {deni.sekolah}')

budi = Pekerja('Budi', 'Pontianak', 'Gugle')
budi.perkenalan()
print(f'Saya bekerja di {budi.tempat_kerja} ')

