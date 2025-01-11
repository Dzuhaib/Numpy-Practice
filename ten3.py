import numpy as np

arr = np.array([1, 2, 3, 4])
# Get third and fourth elements from the following array and add them.
print(arr[2] + arr[3])


# Access the element on the first row, second column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

# Access the element on the 2nd row, 5th column:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])

# Access the third element of the second array of the first array:
arr = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print('3rd element of the second array:' , arr[1, 1, 2])

# Print the last element from the 2nd dim:
arr = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print('Last element from the 2nd Dim:' , arr[0, -1])