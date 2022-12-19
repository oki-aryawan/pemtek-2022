import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

prodi = ['Mat', 'Sta', 'Bio', 'Kim', 'Tek', 'Fis']
mahasiswa = [56, 70, 76, 60, 104, 74]
mahasiswi = [78, 66, 88, 79, 46, 62]
x = np.arange(len(prodi))
width = 0.35
fig, ax = plt.subplots(figsize=(8, 5))
mhsa = ax.bar(x - width/2, mahasiswa, width, label='Laki-laki', color='steelblue')
mhsi = ax.bar(x + width/2, mahasiswi, width, label='Perempuan', color='lightcoral')
ax.set_title('Jumlah Mahasiswa/i Per Program Studi', size=16)
ax.set_ylabel('Jumlah Mahasiswa', size=14)
ax.set_xticks(x)
ax.set_xticklabels(prodi, size=12)
ax.legend(fontsize=14)
plt.show()
