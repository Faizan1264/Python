
def square_numbers(numbers):
    square = []
    for i in numbers:
        square.append(i * i)
    return square


size = int(input("Enter size of list: "))
numbers = []
for i in range(size):
    user_input = int(input("Enter number for list: "))
    numbers.append(user_input)


squared_numbers = square_numbers(numbers)
print(f"The list of squared numbers is: {squared_numbers}")