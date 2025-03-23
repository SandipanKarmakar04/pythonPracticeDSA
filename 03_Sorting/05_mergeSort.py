def conquer(list1, startIndex, mid, endIndex):
    merge = 

def divide(list1, startIndex, endIndex):
    if startIndex >= endIndex:
        return
    
    mid = (startIndex + endIndex) // 2
    divide(list1, startIndex, mid)
    divide(list1, mid+1, endIndex)
    conquer(list1, startIndex, mid, endIndex)

def mergeSort():
    pass

l1 = [1,3,2,9,8,5,6]
mergeSort(l1, 0, len(l1)-1)
print(l1)