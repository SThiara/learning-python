def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  for num in l2:
    l1.remove(num)
  return l1

l1 = removeList()
print(l1)