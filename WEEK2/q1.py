n = int(input("Enter any number "))
rev = 0
temp = n
while(n > 0):
    last = n % 10
    rev = rev * 10 + last
    n = n //10
print("Original number is " , temp ,"\nReverse number is " ,rev) 
