import numpy as np

a = np.array([1,2,8], float)
b = a
a[-1] = 0
a = np.array([1,2,8], float)
b = a
c = a.copy()
a[-1]= 90
print(a)
print(b)
print(c)