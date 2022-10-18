class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.alas

    
segitiga1 = Segitiga(5,10)
segitiga2 = Segitiga(10,10)


print(f'Luas segitiga1: {segitiga1.get_luas()}')
print(f'Luas segitiga2: {segitiga2.get_luas()}')
