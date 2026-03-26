import numpy as np

array1 = np.array([[1, 2, 3, 4]])

array2 = np.array([[1], [2], [3], [4]])

array3 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

print(array1.shape)
print(array2.shape)

print(array1*array2) # (1, 4)*(4, 1) = (4, 4)
print(array2*array3) # (4, 1)*(2, 4) = value error [no broadcasting]

