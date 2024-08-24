n = int(input("Enter any number "))
for i in range(0, n):
    for j in range(n - i, 0, -1):
        print(j , end = " ")
    print()
5
