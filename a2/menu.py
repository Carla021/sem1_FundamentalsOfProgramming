import random


def generateNumbers(n):
    arr=[]
    for i in range(n):
        value = random.randint(0,100)
        arr.append(value)
    return arr

def bubbleSort(arr, n, step1):
    swapped = False
    step = 0
    swapped = True
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            aux = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = aux
            swapped = False
            step += 1
            if step % step1 == 0:
                print(arr)
    while swapped == False:
        swapped = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                aux = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = aux
                swapped = False
                step += 1
                if step % step1 == 0:
                    print(arr)


def stoogeSort(arr, start, end, step2, step):
    if start <= end:
        if arr[start] > arr[end]:
            aux = arr[start]
            arr[start] = arr[end]
            arr[end] = aux
            step += 1
            if step % step2 == 0:
                print(arr)
        if end - start + 1 > 2:
            t = int((end - start + 1)//3)
            stoogeSort(arr, start, end - t, step2, step)
            stoogeSort(arr, start + t, end, step2, step)
            stoogeSort(arr, start, end - t, step2, step)


def main():
    arr = []

    print('press 1 to generate n random numbers')
    print('press 2 to use Bubble Sort')
    print('press 3 to use Stooge Sort')
    print('press 4 to print the list')
    print('press 0 to exit')
    option = int(input())

    while option != 0:

        if option == 1:
            n = int(input())
            arr=generateNumbers(n)
            print(arr)

        if option == 2:
            step1 = int(input())
            bubbleSort(arr, len(arr), step1)

        if option == 3:
            step2 = int(input())
            step = 0
            stoogeSort(arr, 0, len(arr) - 1, step2, step)

        if option == 4:
            print('the sorted list is: ', arr)

        print('press 1 to generate n random numbers')
        print('press 2 to use Bubble Sort')
        print('press 3 to use Stooge Sort')
        print('press 4 to print the list')
        print('press 0 to exit')
        option = int(input())


main()
