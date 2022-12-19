import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
fig = plt.figure('Line Chart')
ax = fig.add_axes([0,0,1,1])
nilai = [80,90,65,79,82]
ax.plot(nilai)
plt.grid()
plt.show()