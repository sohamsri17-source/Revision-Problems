numbers = input(int(" "))

# METHOD 1
def isEven(n):
    return n%2 == 1  
even = filter(isEven, numbers)    
print(list(even))

# METHOD 2
even1 = filter(lambda n : n % 2 == 0, numbers)
print(list(even1))