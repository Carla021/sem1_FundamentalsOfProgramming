'''
Given an array of integers A, maximize the value of the expression
A[m] - A[n] + A[p] - A[q], where m, n, p, q are array indices with m > n > p > q. For A = [30, 5, 15, 18, 30, 40], the maximum value is 32, obtained as 40 - 18 + 15 - 5.
Display both the maximum value as well as the expression used to calculate it.
'''


def findMaxValue(arr, n, maximum):

    if n < 4:
        print("The array should have at least 4 elements")
        return maximum

    for m in range(len(arr)):
        for n in range(m):
            for p in range(n):
                for q in range(p):
                    if arr[m] - arr[n] + arr[p] - arr[q] > maximum:
                        mMax = m
                        nMax = n
                        pMax = p
                        qMax = q
                        maximum = arr[m] - arr[n] + arr[p] - arr[q]

    print(arr[mMax], " - ", arr[nMax], " + ", arr[pMax], " - ", arr[qMax])
    print(maximum)


def main():
    arr = [30, 5, 15, 18, 30, 40]
    n = len(arr)

    maximum = -100000000

    findMaxValue(arr, n, maximum)

main()