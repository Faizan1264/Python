def remove_char(s, index):
    result = s[0:index - 1]
    return result
s = input("Enter any string ")
n = int(input("Enter any number "))
ans = remove_char(s,n)
print(ans)
