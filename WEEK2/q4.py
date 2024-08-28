n = int(input("Enter any number "))
a = 0
b = 1
print(a,b, end = " ")
for i in range(2 , n+1):
    fact = a + b
    print(fact, end = " ")
    a = b
    b = fact
