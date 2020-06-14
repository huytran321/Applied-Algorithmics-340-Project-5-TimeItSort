#Huy Tran
#11/15/2019
#All 6 sorts methods


def bubbleSort(inList):
    for place in range(len(inList) - 1, 0, -1):
        for i in range(place):
            if inList[i] > inList[i + 1]:
                temp = inList[i]
                inList[i] = inList[i + 1]
                inList[i + 1] = temp

def insertionSort(inList):
    for i in range(1, len(inList)):
        currentValue = inList[i]
        position = i

        while position > 0 and inList[position - 1] > currentValue:
            inList[position] = inList[position - 1]
            position = position - 1

            inList[position] = currentValue

def mergeSort(inList):
    if len(inList) > 1:
        mid = len(inList) // 2
        leftHalf = inList[:mid]
        rightHalf = inList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)


        i = 0
        j = 0
        k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                inList[k] = leftHalf[i]
                i = i + 1
            else:
                inList[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            inList[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            inList[k] = rightHalf[j]
            j = j + 1
            k = k + 1

def iterativeMergeSort(inList):
    
    tempList = []

    length = len(inList)
    size = 1
    while size < length:
        size += size
        for position in range(0, length, size):
            subListStart = position
            subListMid = position + (size // 2)
            subListEnd = position + size
            left = inList[subListStart: subListMid]
            right = inList[subListMid: subListEnd]
            inList[subListStart: subListEnd] = merge(left, right)

def merge(left, right):
    result = []
    x = 0
    y = 0
    for i in range(0, len(left) + len(right)):
        if x == len(left):
            result.append(right[y])
            y += 1
        elif y == len(right):
            result.append(left[x])
            x += 1
        elif right[y] < left[x]:
            result.append(right[y])
            y += 1
        else:
            result.append(left[x])
            x += 1
    return result

def quickSort(inList):
    quickSortRec(inList, 0, len(inList) - 1)

def quickSortRec(inList, first, last):
    if last - first < 5:
        insertionSortPartialList(inList, first, last)
        return

    mid = (first + last) // 2
    if inList[first] > inList[last]:
        inList[first], inList[last] = inList[last], inList[first]

    elif inList[first] > inList[mid]:
        inList[first], inList[mid] = inList[mid], inList[first]

    elif inList[mid] > inList[last]:
        inList[mid], inList[last] = inList[last], inList[mid]

    pivot = inList[mid]
    inList[mid], inList[last - 1] = inList[last - 1], inList[mid]

    left = first + 1
    right = last - 2
    done = False

    while not done:
        while inList[left] < pivot:
            left += 1
        while inList[right] > pivot:
            right -= 1
        if right > left:
            inList[left], inList[right] = inList[right], inList[left]
            right -= 1
            left += 1
        else:
            done = True

    inList[left], inList[last - 1] = inList[last - 1], inList[left]
    quickSortRec(inList, first, left - 1)
    quickSortRec(inList, left + 1, last)

def insertionSortPartialList(inList, first, last):
    for place in range(first + 1, last):
        temp = inList[place]
        i = place
        while i > 0 and inList[i -1] > temp:
            inList[i] = inList[i - 1]
            i = i - 1
        inList[i] = temp


def shellSort(inList):
    size = len(inList)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = inList[i]
            j = i
            while j >= gap and temp < inList[j - gap]:
                inList[j] = inList[j - gap]
                j -= gap
                inList[j] = temp
        if gap == 2:
            gap = 1
        else:
            gap = int(gap / 2.2)



