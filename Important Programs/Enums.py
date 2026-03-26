from enum import Enum
    
class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Colour(2))
print(list(Colour))
