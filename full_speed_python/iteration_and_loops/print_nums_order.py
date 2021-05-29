def printEvenOdd(n):
    if n == 0:
        return
    if n % 2 == 0:
        print ("Even number: " + str(n))
    else:
        print ("Odd number: " + str(n))
    printEvenOdd(n-1)


printEvenOdd(10)