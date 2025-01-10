import numpy as np

a = np.array(42)
# 1 - D Array
b = np.array([1,2,3,4,5,6])
# 2 - D Arary
c = np.array([[1,2,3],[4,5,6]])
# 3 - D Array
d = np.array([[[1,2,3,], [4,5,6], [1,2,3], [4,5,6]]])

print(a.ndim)
print(b.ndim)   
print(c.ndim)
print(d.ndim)

print(d[0,1,2])