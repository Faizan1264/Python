def cal_sum_sub(a, b):
   addition = a + b
   subtraction = a - b
   return addition, subtraction


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


result_add, result_sub = cal_sum_sub(num1, num2)

print(f"The sum of {num1} and {num2} is: {result_add}")
print(f"The difference between {num1} and {num2} is: {result_sub}")