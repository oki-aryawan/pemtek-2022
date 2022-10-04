"""
Soal Tipe B Ujian Tengah Semester
Mata Kuliah Pemrograman Teknik 2022/2023
copied by: Oki Aryawan
"""

n = 0
obj = ['sun', 'moon', 'star', 'meteor', 'comet']
for x in obj:
    x = x + obj[n]
    n = n + 3
    print(x)
    if n >= len(obj):
        break
del(obj[n-5])
print(obj[1:3])