class Wrapper:
    def __getattribute__(self, name):
         self.name = name
         