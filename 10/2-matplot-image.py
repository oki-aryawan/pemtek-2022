from matplotlib import pyplot as plt
import cv2
path = 'file/kucing.PNG'
im = cv2.imread(path)
color = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
plt.imshow(color)
plt.title('Kuy')
plt.show()