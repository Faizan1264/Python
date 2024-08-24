s = input("Enter any string ")
length = len(s)
for i in range(length):
    if(i % 2 == 0):
        print(s[i], end = " ")
