import cv2

path = 'file/kucing.PNG'
img = cv2.imread(path)
cv2.imshow('Membuka Gambar', img)
cv2.waitKey(0)
cv2.destroyAllWindows()