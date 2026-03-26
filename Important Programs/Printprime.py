# Write a Python program that asks the user to enter a positive integer N, and print the first N prime numbers starting from 2.

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
