import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.style.use('ggplot')
X = np.linspace(0, 6.27, 360)
y1 = np.cos(X)
y2 = np.sin(X)
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(y1, y2, color='orange')
#ax.plot(X, y2, color='blue')
plt.show()
