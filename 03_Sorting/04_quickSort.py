def partition(list1, low, high):
    pivot = list1[high]
    i = low-1

    for j in range(low, high):
        if list1[j] < pivot:
            i += 1
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
    i += 1
    temp = list1[i]
    list1[i] = pivot
    list1[high] = temp
    return i

def quickSort(list1, low, high):
    if low < high:
        pivotIndex =  partition(list1, low, high)
        quickSort(list1, low, pivotIndex-1)
        quickSort(list1, pivotIndex+1, high)

l1 = [1,3,2,9,8,5,6]
quickSort(l1, 0, len(l1)-1)
print(l1)