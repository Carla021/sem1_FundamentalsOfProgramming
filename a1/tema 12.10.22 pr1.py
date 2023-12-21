import math

def isPrime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n = int(input())
n = n + 1

while isPrime(n) == False:
    n += 1

print(n)

