import matplotlib.pyplot as plt
fig = plt.figure('Line Chart')
ax = fig.add_axes([0.5,0.5,1,1])
nilai = [80,90,65,79,82]
ax.plot(nilai)
plt.show()