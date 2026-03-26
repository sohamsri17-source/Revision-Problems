def is_palindrome_string(number):
    
    num_str = str(number)
    return num_str == num_str[::-1]

# Example usage:
num1 = 121
num2 = 12345
num3 = 9009

print(f"{num1} is a palindrome: {is_palindrome_string(num1)}")
print(f"{num2} is a palindrome: {is_palindrome_string(num2)}")
print(f"{num3} is a palindrome: {is_palindrome_string(num3)}")


        