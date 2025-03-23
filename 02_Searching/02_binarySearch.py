li = [1,2,3,4,5,6,7,8,9]

val = int(input("Enter a value to search: "))

low = 0
high = len(li)-1
while (low <= high):
    mid = (low + high) // 2
    if li[mid] == val:
        print ("value is found",li[mid])
    if (li[mid] < val):
        low = mid +1
    else:
        high = mid - 1
    
