import numpy as np
a = np.array([1, 2, 8], float)
b = np.array([4, 5, 6], float)
c = np.array([7, 8, 9, 10], float)
print(np.concatenate((a, b, c)))
print("\n")

a = np.array([[1, 2, 3], [7, 8, 9]], float)
b = np.array([[4, 5, 6], [7, 8, 10]], float)
print(np.concatenate((a, b), axis=0))
print(np.concatenate((a, b), axis=1))
print("\n")

a = np.array([1, 2, 8], float)
print(a)
print(a[:, np.newaxis], a[:, np.newaxis].shape)
print(a[np.newaxis, :], a[np.newaxis, :].shape)