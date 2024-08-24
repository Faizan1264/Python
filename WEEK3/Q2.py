n = int(input("Enter any number "))
for i in range(1, n + 1):
    for j in range(0, i):
        print("*" , end = " ")
    print()
for i in range(1, n + 1):
    for j in range(n - i , 0 , -1):
        print("*" , end = " ")
    print()