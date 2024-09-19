def count_occurrences(tup, item):
    return tup.count(item)

# 5
# userinput
l = []
for i in range( 5):
    x = int(input("Enter tuple data "))
    l.append(x)
t = tuple(l)
item_to_count = int(input("Enter the number you want to count "))

occurrences = count_occurrences(t, item_to_count)
print(f"The number {item_to_count} occurs {occurrences} times in the tuple.")