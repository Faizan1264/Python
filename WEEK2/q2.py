n = int(input("Enter any number "))
count = 0
temp = n
while( n != 0):
    last = n % 10
    count += 1
    n = n//10
print("Total number of digits in " , temp , " is " ,   count)
