def getSquare():
 l1=[ x**2 for x in range(0, 21, 2) if x % 3 != 0] 
 #l1 = [num for num in [num**2 for num in range(0, 21, 2)] if (num % 3 != 0)]
 return l1

print(getSquare())