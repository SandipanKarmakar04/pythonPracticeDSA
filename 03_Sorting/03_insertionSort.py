def insertionSort(list1): 
    for i in range(1, len(list1)):
        temp = list1[i]

        prev = i-1
        while prev >= 0 and list1[prev] > temp:
            list1[prev+1] = list1[prev]
            prev -= 1
        list1[prev+1] = temp

l1 = [4,1,5,2,3]
insertionSort(l1)
print(l1)