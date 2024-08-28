n = int(input("Enter any number "))
temp = n
sum = 0
while(n != 0):
    last = n % 10
    sum += last
    n = n//10
print("sum of digits of ", temp , " is " , sum)
