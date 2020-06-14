
#Huy Tran
#11/15/2019
#Sort Driver, Timit code is shown above, Below is the Driver code for the command Line

import sort
import random
import time
import timeit

def bubbleSortTime():
    
    SETUP_CODE = '''
import sort
import random
testList = []
for i in range(50000):
    testList.append(random.randint(0,1000))'''

    TEST_CODE = '''
sort.bubbleSort(testList)'''

    times = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 1, number = 1)

    print('bubbleSortTime: {}'.format(min(times)))

def insertionSortTime():
    
    SETUP_CODE = '''
import sort
import random
testList = []
for i in range(50000):
    testList.append(random.randint(0,1000))'''

    TEST_CODE = '''
sort.insertionSort(testList)'''

    times = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 1, number = 1)

    print('insertionSortTime: {}'.format(min(times)))

def mergeSortTime():
    
    SETUP_CODE = '''
import sort
import random
testList = []
for i in range(50000):
    testList.append(random.randint(0,1000))'''

    TEST_CODE = '''
sort.mergeSort(testList)'''

    times = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 1, number = 1)

    print('mergeSortTime: {}'.format(min(times)))

def iterativeMergeSortTime():
    
    SETUP_CODE = '''
import sort
import random
testList = []
for i in range(25000):
    testList.append(random.randint(0,1000))'''

    TEST_CODE = '''
sort.iterativeMergeSort(testList)'''

    times = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 1, number = 1)

    print('iterativeMergeSortTime: {}'.format(min(times)))

def quickSortTime():
    
    SETUP_CODE = '''
import sort
import random
testList = []
for i in range(50000):
    testList.append(random.randint(0,1000))'''

    TEST_CODE = '''
sort.quickSort(testList)'''

    times = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 1, number = 1)

    print('quickSortTime: {}'.format(min(times)))

def shellSortTime():
    
    SETUP_CODE = '''
import sort
import random
testList = []
for i in range(50000):
    testList.append(random.randint(0,1000))'''

    TEST_CODE = '''
sort.shellSort(testList)'''

    times = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 1, number = 1)

    print('shellSortTime: {}'.format(min(times)))

#bubbleSortTime()
#insertionSortTime()
#mergeSortTime()
#quickSortTime()
#shellSortTime()
#iterativeMergeSortTime()


#Sys code for the command line

import sys

if len(sys.argv) < 2:
    print()
elif sys.argv[1] == "BubbleSort":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0,10000))
            print(testList, "\n")
            sort.bubbleSort(testList)
            print(testList)
    else:
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0,10000))
        sort.bubbleSort(testList)
        print("LIST SORTED")

elif sys.argv[1] == "InsertionSort":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0,10000))
            print(testList, "\n")
            sort.insertionSort(testList)
            print(testList)
    else:
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0,10000))
        sort.insertionSort(testList)
        print("LIST SORTED")

elif sys.argv[1] == "MergeSort":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0,10000))
            print(testList, "\n")
            sort.mergeSort(testList)
            print(testList)
    else:
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0,10000))
        sort.mergeSort(testList)
        print("LIST SORTED")

elif sys.argv[1] == "IterativeMergeSort":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0,10000))
            print(testList, "\n")
            sort.iterativeMergeSort(testList)
            print(testList)
    else:
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0,10000))
        sort.iterativeMergeSort(testList)
        print("LIST SORTED")

elif sys.argv[1] == "QuickSort":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0,10000))
            print(testList, "\n")
            sort.quickSort(testList)
            print(testList)
    else:
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0,10000))
        sort.quickSort(testList)
        print("LIST SORTED")

elif sys.argv[1] == "ShellSort":
    if len(sys.argv) > 3: 
        if sys.argv[3] == "PRINT":
            testList = []
            for i in range(int(sys.argv[2])):
                testList.append(random.randint(0,10000))
            print(testList, "\n")
            sort.shellSort(testList)
            print(testList)
    else:
        testList = []
        for i in range(int(sys.argv[2])):
            testList.append(random.randint(0,10000))
        sort.shellSort(testList)
        print("LIST SORTED")
else:
    print("\n" + "Please retype with the correct order or notation shown in the file")







