import numpy as np

# sLice elements from index 1 to index 5 from the following array:
arr = np.array([1,2,3,4,5,6,7,8])

print(arr[1:4])

# duplicate an array using slice index 1 to 4 now new arrays contains index 1 to 4 excluding last element.
arr1 = arr[1:4]

print('Duplicating the array with slice elememt index 1 to 4: ', arr1)

# sLice elements from the start to index 4 from the following array excluding last element:
arr = np.array([1,2,3,4,5,6,7])
print(arr[:4])

# Slice from the index 4 from the end to index 1 from the end:
arr = np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])4