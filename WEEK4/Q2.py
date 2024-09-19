def check_first_last(numbers):
    first_num = numbers[0]
    last_num = numbers[-1]
    result = True if(first_num == last_num) else False
    return result

n = int(input("Enter size of list "))
numbers = []
for i in range (n):
    x = int(input("Enter list Numbers "))
    numbers.append(x)

result = check_first_last(numbers)

if result:
    print("True - The first and last numbers are the same.")
else:
    print("False - The first and last numbers are different.")