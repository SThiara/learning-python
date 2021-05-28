def evenSquareSum():
  even = [x**2 for x in range(0, 21, 2)]
  return sum(even)
  
print(evenSquareSum())