"""
Soal Tipe B Ujian Tengah Semester
Mata Kuliah Pemrograman Teknik 2022/2023
copied by: Oki Aryawan
"""


x = 33.3
val = int(x/3-2**3)
print(x,'xxx',val)
count = 0

while val > 0:
    if val % 2 != 1:
        val = val/2
    else:
        val = val - 1
    count = count + 1
print('Hasil val: ', val)
print('Count: ', count)

