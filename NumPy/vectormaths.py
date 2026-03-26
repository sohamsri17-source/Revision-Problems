import numpy as np

# Vectorised Math Functions 

# Area of circle = (pie)(r)^2
radii = np.array([1.01, 2.5, 3.99])
print(np.pi * radii ** 2 )

# Some math functions
print(np.sqrt(radii))
print(np.ceil(radii))
print(np.round(radii))
print(np.floor(radii))