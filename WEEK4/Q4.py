from itertools import zip_longest
def iterate_lists(list1, list2):
    # Iterate over both lists simultaneously
    for i, j in zip_longest(list1, reversed(list2),  fillvalue=" "):
        # print(f"List 1 item: {item1}, List 2 item: {item2}")
        print(i, j)
    

size1 = int(input("Enter size of list 1 "))
l1 = []

for i in range(size1):
    x = int(input("Enter numbers for list1 "))
    l1.append(x)
size2 = int(input("Enter size of list 2 "))
l2 = []
for j in range(size2):
    x = int(input("Enter numbers for list1 "))
    l2.append(x) 
iterate_lists(l1, l2)

