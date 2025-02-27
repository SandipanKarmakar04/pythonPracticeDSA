def bubbleSort(dataList):
    for i in range (1, len(dataList)):
        for j in range(len(dataList)-i):
            if dataList[j] > dataList[j+1]:
                dataList[j], dataList[j+1] = dataList[j+1], dataList[j]

li = [3,2,8,1,5]
bubbleSort(li)
print(li)
