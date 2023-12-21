import random
import timeit
from decimal import Decimal


def generateNumbers(n):
    arr=[]
    for i in range(n):
        value = random.randint(0,100)
        arr.append(value)
    return arr


def bubbleSort(arr, n):
    swapped = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            aux = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = aux
            swapped = False
    while swapped == False:
        swapped = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                aux = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = aux
                swapped = False


def stoogeSort(arr, start, end):
    if start <= end:
        if arr[start] > arr[end]:
            aux = arr[start]
            arr[start] = arr[end]
            arr[end] = aux
        if end - start + 1 > 2:
            t = int((end - start + 1)//3)
            stoogeSort(arr, start, end - t)
            stoogeSort(arr, start + t, end)
            stoogeSort(arr, start, end - t)


def createList(n):
    lists = []
    for i in range(5):
        lists.append(generateNumbers(n))
        n *= 2
    return lists


def main():
    arr = []

    print('press 1 to generate n random numbers')
    print('press 2 to use Bubble Sort')
    print('press 3 to use Stooge Sort')
    print('press 4 to print the list')
    print('press 5 for best case, worst case or average case')
    print('press 0 to exit')
    option = int(input())

    while option != 0:

        if option == 1:
            n = int(input())
            arr=generateNumbers(n)
            print(arr)

        if option == 2:
            bubbleSort(arr, len(arr))

        if option == 3:
            stoogeSort(arr, 0, len(arr) - 1)

        if option == 4:
            print('the sorted list is: ', arr)

        if option == 5:
            print('press 1 for Best Case;')
            print('press 2 for Worst Case;')
            print('press 3 for Average Case:')
            print('press 0 to exit')
            opt = int(input())
            lists = createList(50)
            while opt != 0:
                if opt == 1:
                    print('Bubble Sort:')
                    for list in lists:
                        list.sort()
                    for list in lists:
                        start_Bubble = timeit.default_timer()
                        bubbleSort(list, len(list))
                        end_Bubble = timeit.default_timer()
                        result = Decimal(float("%.6f" % (end_Bubble - start_Bubble)))
                        print(str(len(list)) + ' elements: ' + 'Bubble Sort: ' + str(result))
                    print('Stooge Sort:')
                    for list in lists:
                        list.sort()
                    for list in lists:
                        start_Stooge = timeit.default_timer()
                        stoogeSort(list, 0, len(list) - 1)
                        end_stooge = timeit.default_timer()
                        result = Decimal(float("%.6f" % (end_stooge - start_Stooge)))
                        print(str(len(list)) + ' elements:' + ' Stooge Sort: ' + str(result))
                if opt == 2:
                    print('Bubble Sort:')
                    for list in lists:
                        list.sort(reverse=True)
                    for list in lists:
                        start_Bubble = timeit.default_timer()
                        bubbleSort(list, len(list))
                        end_Bubble = timeit.default_timer()
                        result = Decimal(float("%.6f" % (end_Bubble - start_Bubble)))
                        print(str(len(list)) + ' elements: ' + 'Bubble Sort: ' + str(result))
                    print('Stooge Sort:')
                    for list in lists:
                        list.sort(reverse=True)
                    for list in lists:
                        start_Stooge = timeit.default_timer()
                        stoogeSort(list, 0, len(list) - 1)
                        end_stooge = timeit.default_timer()
                        result = Decimal(float("%.6f" % (end_stooge - start_Stooge)))
                        print(str(len(list)) + ' elements:' + ' Stooge Sort: ' + str(result))
                if opt == 3:
                    print('Bubble Sort:')
                    random.shuffle(list)
                    for list in lists:
                        start_Bubble = timeit.default_timer()
                        bubbleSort(list, len(list))
                        end_Bubble = timeit.default_timer()
                        result = Decimal(float("%.6f" % (end_Bubble - start_Bubble)))
                        print(str(len(list)) + ' elements: ' + 'Bubble Sort: ' + str(result))
                    print('Stooge Sort:')
                    random.shuffle(list)
                    for list in lists:
                        start_Stooge = timeit.default_timer()
                        stoogeSort(list, 0, len(list) - 1)
                        end_stooge = timeit.default_timer()
                        result = Decimal(float("%.6f" % (end_stooge - start_Stooge)))
                        print(str(len(list)) + ' elements:' + ' Stooge Sort: ' + str(result))
                print('press 1 for Best Case;')
                print('press 2 for Worst Case;')
                print('press 3 for Average Case:')
                print('press 0 to exit')
                opt = int(input())

        print('press 1 to generate n random numbers')
        print('press 2 to use Bubble Sort')
        print('press 3 to use Stooge Sort')
        print('press 4 to print the list')
        print('press 5 for best case, worst case or average case')
        print('press 0 to exit')
        option = int(input())


main()
