num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def calc_sum():
    sum = num1 + num2
    return sum

def calc_avg():
     avg = float((num1 + num2)/2)
     return avg

result_sum = calc_sum()
print("Sum is :",result_sum)

result_avg = calc_avg()
print("Average is :",result_avg)