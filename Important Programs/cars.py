# Create 2 Car objects with different color and speed. Show how each has unique data.

class Cars:
    def __init__(self, color, speed):  # Parameterised Constructor
        self.color = color
        self.speed = speed
    
    def display_info(self):  # Method to show car details
        print(f"Color: {self.color}, Speed (in km/hrs): {self.speed}")

# Creating multiple objects using constructor
car1 = Cars("Black", 300)
car2 = Cars("Red", 400)

# Call method 
car1.display_info()
car2.display_info()
