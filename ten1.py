import numpy as np

# Adding demensions number in the array
arr = np.array([1,2,3,4], ndmin=2)

print(arr)

print('number of demensions :', arr.ndim)