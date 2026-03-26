import numpy as np

array  = np.array([['A', 'B', 'C'], 
                   ['D', 'E', 'F'], 
                   ['G', 'H', 'I']])

print(array.ndim)
print(array.shape)
print(array[0][0]) # Chain Indexing
print(array[0, 0]) # Multidimensional Indexing (Faster than chain indexing)