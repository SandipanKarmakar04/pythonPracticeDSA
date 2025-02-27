def selectionSort(list1):
    n = len(list1)
    for i in range (n):
        minIndex = i
        for j in range(i+1,n):
            if list1[j] < list1[minIndex]:
                minIndex = j
        list1[i],list1[minIndex] = list1[minIndex],list1[i]

l1 = [1,3,2,9,8,5,6]
selectionSort(l1)
print(l1)