li = [5, 6, 4, 9, 2, 3]
li.sort()

val = int(input("Enter a value to search: "))

low = 0
high = len(li)-1
while (low <= high):
    mid = (low + high) // 2
    if li[mid] == val:
        print ("value is found",li[mid])
        break
    if (li[mid] < val):
        low = mid +1
    else:
        high = mid - 1
else:
    print("value not found")
