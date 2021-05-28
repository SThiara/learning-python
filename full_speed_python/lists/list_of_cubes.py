def getCube():
  #l1 = [pow(num, 3) for num in range(1, 21)]
  l1 = [num**3 for num in range(1, 21)]
  return l1
l1 = getCube()
print(l1)