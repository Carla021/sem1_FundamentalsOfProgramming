'''
Given an array of integers A, maximize the value of the expression
A[m] - A[n] + A[p] - A[q], where m, n, p, q are array indices with m > n > p > q. For A = [30, 5, 15, 18, 30, 40], the maximum value is 32, obtained as 40 - 18 + 15 - 5.
Display both the maximum value as well as the expression used to calculate it.
'''

def maxValue(arr, n, MIN):
    if n < 4:
        print("The array should have at least 4 elements")
        return MIN

    firstPart = [MIN] * (n + 1)
    secondPart = [MIN] * n
    thirdPart = [MIN] * (n - 1)
    fourthPart = [MIN] * (n - 2)

    #firstPart stores the maximum value of a[m]
    for i in range(n - 1, -1, -1):
        firstPart[i] = max(firstPart[i + 1], arr[i])

    a = firstPart[0]

    #secondPart stores the maximum value of a[m] - a[n]
    for i in range(n - 2, -1, -1):
        secondPart[i] = max(secondPart[i + 1], firstPart[i + 1] - arr[i])

    b = firstPart[0] - secondPart[0]

    #thirdPart stores the maximum value of a[m] - a[n] + a[p]
    for i in range(n - 3, -1, -1):
        thirdPart[i] = max(thirdPart[i + 1], secondPart[i + 1] + arr[i])

    c = thirdPart[0] - secondPart[0]

    #fourthPart stores the maximum value of a[m] - a[n] + a[p] - a[q]
    for i in range(n - 4, -1, -1):
        fourthPart[i] = max(fourthPart[i + 1], thirdPart[i + 1] - arr[i])

    d = thirdPart[0] - fourthPart[0]

    print(a, " - ", b, " + ", c, " - ", d)

    #maximum value in fourthPart[0]
    return fourthPart[0]


def main():
    arr = [30, 5, 15, 18, 30, 40]
    n = len(arr)
    MIN = -100000000
    print(maxValue(arr, n, MIN))


main()

'''
Time Complexity : O(n), where n is the size of input array 
Since we are creating four lists to store our values, space is 4*O(n) = O(4*n) = O(n)
'''