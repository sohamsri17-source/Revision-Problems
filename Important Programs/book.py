# Define a Book class with __init__ taking title and author. Add a display_info method. Add pages parameter and a read_status() method that returns True if pages > 300

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def read_status(self):
        if self.pages > 300:
            return True
        else:
            return False

display_info = Book("The Vegetarian", "By Han Kang", 200)
print(display_info.title)
print(display_info.author)
print(display_info.read_status())